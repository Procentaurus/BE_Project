import scrapy
from ..support import read_col_from_csv
from ..items import ProductItem
from bs4 import BeautifulSoup
from random import random, randint
import requests

class ProductSpider(scrapy.Spider):

    name = "product_spider"

    custom_settings = {
        'FEEDS': {
            'C:\\PG\\sem_5\\BE\\Project\\ScrapResults\\product_data.csv': {
                'format': 'csv',
                'overwrite': True,
                'encoding': 'utf8',
            }
        },
        'FEED_EXPORTERS': {
            'csv': 'scraper.exporters.CustomCsvItemExporter',
        }
    }

    def start_requests(self):
        
        path_to_storage = "C:\\PG\\sem_5\\BE\Project\\ScrapResults\\"
        base_url = "https://www.centrumrowerowe.pl"
        product_paths = read_col_from_csv('{}\\data.csv'.format(path_to_storage), "product_site_path")
        sub_categories = read_col_from_csv('{}\\data.csv'.format(path_to_storage), "sub_category")

        for i in range(10):
            yield scrapy.Request(base_url + product_paths[i], callback=self.parse, cb_kwargs={'sub_category': sub_categories[i]} )


    def parse(self, response, sub_category):
        
        base_url = "https://www.centrumrowerowe.pl"
        body_element = response.css('body')
        body_class = body_element.css('::attr(class)').get()

        name = ""
        price = ""
        description = ""
        brand = ""
        color = ""
        product_code = ""

        if body_class != "notFound":

            name = response.xpath('//h1/text()').get()

            price_elem = response.css('.int-part')
            price = price_elem.css('::text').get()

            description_elems = response.css('.fr-wrapper p')

            for description_elem in description_elems:
                html_content = description_elem.extract()
                soup = BeautifulSoup(html_content, 'html.parser')
                text = soup.get_text()
                text = text.replace('\r\n', '\\r\\n')
                
                description += text

            image_path_1 = base_url + response.css('.standard img::attr(src)').get()
            image_path_2 = image_path_1[:-5] + '2' + image_path_1[-4:]

            def check_url(url):
                try:
                    response = requests.get(url)
                    return response.status_code == 200
                except requests.RequestException:
                    return False


            li_tag_brand = response.xpath('//div[@class="prod-feature"]/ul/li[span[@class="label" and text()="Marka"]]')
            li_tag_color = response.xpath('//div[@class="prod-feature"]/ul/li[span[@class="label" and text()="Kolor"]]')
            li_tag_code = response.xpath('//div[@class="prod-feature"]/ul/li[span[@class="label" and text()="Kod produktu"]]')

            color = li_tag_color.xpath('./span[@class="value"]/text()').get() if li_tag_color.xpath('./span[@class="value"]/text()').get() else li_tag_color.xpath('./span[@class="value"]/a/text()').get()
            product_code = li_tag_code.xpath('./span[@class="value"]/text()').get()
            brand = li_tag_brand.xpath('./span[@class="value"]/a/text()').get()

            item = ProductItem()
            item["Product_ID"] = product_code
            item["Active"] = 1
            item["Name"] = name if name is not None else ""
            item["Wholesale_price"] = price + ".99"
            item["Weight"] = round(random() * 3, 3)
            item["Delivery_time_of_in_stock_products"] = randint(2, 10)
            item["Quantity"] = randint(0, 10)
            item["Description"] = description if description is not None else ""
            item["Available_for_order"] = 0 if item["Quantity"] == 0 else 1
            item["Image_URLs"] = image_path_1, image_path_2 if check_url(image_path_2) else image_path_1
            item["Manufacturer"] = brand
            item['Categories'] = sub_category
            item["Color"] = f"Color:{color}:0"

            yield item