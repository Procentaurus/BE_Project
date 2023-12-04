from copy import deepcopy
from pprint import pprint
import csv
from utils import *
from urllib.parse import quote
from urllib.request import urlretrieve
from prestapyt import PrestaShopWebServiceDict
import os
from timeit import default_timer as timer

BLANK_SCHEMA_PATH = 'product_blank.xml'
PRODUCT_DATA_PATH = 'ScrapResults\\product_data.csv'
IMAGES_FOLDER_PATH = 'tmp\\images\\'

class ProductInitializer():

    def __init__(self, ps: PrestaShopWebServiceDict):
        self.ps = ps
        f = open(BLANK_SCHEMA_PATH, 'r')
        string = f.read()
        f.close()
        blank = ps._parse(string)
        self.blank = blank['prestashop']
        self.categories = {}

    def initialize_products(self):

        # TODO(Potentially) Initialize color feature

        with open(PRODUCT_DATA_PATH, newline='', encoding='utf-8') as csvfile:

            reader = csv.DictReader(csvfile, delimiter=';')

            i = 0
            time_sum = 0

            for row in reader:

                time = timer()
                self.initialize_product(row)
                time = timer() - time

                time_sum += time

                i += 1

                average = time_sum/i
                est = average * (1096-i)

                os.system('cls')
                print(str(i) + '/1096 ' + str((i/1096) * 100) + '%')
                print('Estimated time remaining: ' + str(est) + ' Average time: ' + str(average))
                

    def initialize_product(self, row):
        product = deepcopy(self.blank)

        id = self.lookup_category_id(row['Categories'])

        product['product'].update({
            'id_category_default': id,
            'weight': row['Weight'],
            'state': '1',
            'price': row['Wholesale_price'].replace(' ', ''),
            'active': '1',
            'available_for_order': row['Available_for_order'],
            'show_price': '1',
            'name': language_wrapper(row['Name']),
            'description': language_wrapper(row['Description']),            
        })

        product['product']['associations'].update({
            'categories': category_wrapper(id),
            # 'product_features': {
            #     'product_feature': {
            #         'id': '1',
            #         'id_feature_value': '0',
            #     },
            # },
        })

        product = self.ps.add('products', product)['prestashop']

        # Add the quantity

        id_stock_available = get_stock_available_id(product)
        self.update_stock_quantity(id_stock_available, row['Quantity'])

        # Add the image

        self.add_product_images(product['product']['id'], row['Image_URLs'].split(','))

    def update_stock_quantity(self, id, value):
        stock_available = self.ps.get('stock_availables', id)
        stock_available['stock_available'].update({
            'quantity': value
        })
        self.ps.edit('stock_availables', stock_available)

    def add_product_images(self, id, images_urls):
        for url in images_urls:

            # Download the image

            img_name = str(hash(url)) + '.png'
            img_path = IMAGES_FOLDER_PATH + img_name
            urlretrieve(url, img_path)

            # Read the image

            f = open(img_path, 'rb')
            content = f.read()
            f.close()

            # Send it to the API

            self.ps.add('/images/products/' + id, files=[('image', img_name, content)])

            # Delete it from the system

            os.remove(img_path)

    def lookup_category_id(self, name):
        id = self.categories.get(name)

        if id == None:
            id = get_category_id(
                self.ps.get('categories', options={'filter[name]': name})
            )
            self.categories[name] = id

        return id