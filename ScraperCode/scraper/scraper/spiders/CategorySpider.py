import scrapy
from ..items import CategoryItem

class CategorySpider(scrapy.Spider):

    name = "category_spider"

    custom_settings = {
        'FEEDS': { 'C:\\PG\\sem_5\\BE\\Project\\ScrapResults\\category_data.csv': {
            'format': 'csv',
            'overwrite': True,
            'encoding': 'utf8',
            'csv_delimiter': ';'
        }},
        'FEED_EXPORTERS': {
            'csv': 'scraper.exporters.CustomCsvItemExporter',
        }
    }

    def start_requests(self):

        categories = ["warsztat-rowerowy", "akcesoria", "czesci", "odziez-rowerowa"]
        categories_pl = ["warsztat rowerowy", "akcesoria", "części", "odzież rowerowa"]
        sub_categories = [
            ["stojaki-serwisowe-na-rower", "narzedzia-rowerowe"],
            ["blotniki-rowerowe", "bagazniki-rowerowe"],
            ["grupy-osprzetu", "rowerowe-napinacze-lancucha"],
            ["bielizna-rowerowa", "bluzy-rowerowe"]
        ]
        sub_categories_pl = [
            ["stojaki serwisowe na rower", "narzędzia-rowerowe"],
            ["błotniki rowerowe", "bagażniki rowerowe"],
            ["grupy osprzętu", "rowerowe napinacze łańcucha"],
            ["bielizna rowerowa", "bluzy rowerowe"]
        ]
        
        base_url = "https://www.centrumrowerowe.pl/"
        counter = 0

        for i in range(len(categories)):
            for j in range(len(sub_categories[0])):
                url = "{}/{}/{}/".format(base_url, categories[i], sub_categories[i][j])
                counter += 1
                yield scrapy.Request(url, callback=self.parse_sub_category, cb_kwargs={'sub_category': sub_categories_pl[i][j], 'category': categories_pl[i], 'id':counter})

        for i in range(len(categories)):
            counter += 1
            yield scrapy.Request(url, callback=self.parse_category, cb_kwargs={'category': categories_pl[i], 'id':counter})

    def parse_sub_category(self, response, sub_category, category, id):

        body_element = response.css('body')
        body_class = body_element.css('::attr(class)').get()

        if body_class != "notFound":

            description = body_element.css('.description.top.collapse p::text').get()

            item = CategoryItem()

            item['Category_ID'] = id
            item['Active'] = 1
            item['Name'] = sub_category
            item['Description'] = description
            item['Parent_category'] = category
            item['Root_category'] = 0

            yield item

    def parse_category(self, response, category, id):

        body_element = response.css('body')
        body_class = body_element.css('::attr(class)').get()

        if body_class != "notFound":

            description = body_element.css('.description.top.collapse p::text').get()

            item = CategoryItem()

            item['Category_ID'] = id
            item['Active'] = 1
            item['Name'] = category
            item['Description'] = description
            item['Parent_category'] = ""
            item['Root_category'] = 1

            yield item