from copy import deepcopy
import csv
from utils import *
from urllib.parse import quote
from prestapyt import PrestaShopWebServiceDict

BLANK_SCHEMA_PATH = 'category_blank.xml'
CATEGORY_DATA_PATH = 'ScrapResults\\category_data.csv'

class CategoryInitializer():

    def __init__(self, ps: PrestaShopWebServiceDict):
        self.ps = ps
        f = open(BLANK_SCHEMA_PATH, 'r')
        string =  f.read()
        f.close()
        blank = ps._parse(string)
        self.blank = blank['prestashop']

    def initialize_categories(self):
        with open(CATEGORY_DATA_PATH, newline='', encoding='utf-8') as csvfile:

            # Initialize root categories

            reader = csv.DictReader(csvfile, delimiter=';')

            for row in reader:
                if row['Parent_category'] == 'Strona główna':
                    self.initialize_category(row)

        with open(CATEGORY_DATA_PATH, newline='', encoding='utf-8') as csvfile:
            
            # Initialize remaining categories

            reader = csv.DictReader(csvfile, delimiter=';') # Reloading the reader

            for row in reader:
                if row['Parent_category'] != 'Strona główna':
                    id_parent = get_category_id(
                        self.ps.get('categories', options={'filter[name]': row['Parent_category']})
                    )
                    self.initialize_category(row, id_parent)
          
    def initialize_category(self, row, id_parent='2'):
        category = deepcopy(self.blank)

        category['category'].update({
            'id_parent': id_parent,
            'active': '1',
            'name': language_wrapper(row['Name']),
            'link_rewrite': language_wrapper(quote(row['Name'].replace(' ', '-'))),
            'description': language_wrapper(row['Description']),
        })

        self.ps.add('categories', category)