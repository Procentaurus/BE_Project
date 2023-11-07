import scrapy
from ..support import read_col_from_csv
from ..items import DetailItem
from ..pipelines import *
from bs4 import BeautifulSoup

class DetailSpider(scrapy.Spider):

    name = "detail_spider"

    custom_settings = {
        'FEEDS': { 'F:\\184725\\ScrapResults\\final_data.csv': {
            'format': 'csv',
            'overwrite': True,
            'encoding': 'utf8'
        }}
    }

    def start_requests(self):
        
        path_to_storage = "F:\\184725\\ScrapResults\\"
        base_url = "https://www.centrumrowerowe.pl"
        product_paths = read_col_from_csv('{}\\data.csv'.format(path_to_storage), "product_site_path")

        for i in range(10):
            yield scrapy.Request(base_url + product_paths[i], callback=self.parse)

    def parse(self, response):
        
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

            image_path_1 = response.css('.standard img::attr(src)').get()
            image_path_2 = image_path_1[:-5] + '2' + image_path_1[-4:]

            li_tag_brand = response.xpath('//div[@class="prod-feature"]/ul/li[span[@class="label" and text()="Marka"]]')
            li_tag_color = response.xpath('//div[@class="prod-feature"]/ul/li[span[@class="label" and text()="Kolor"]]')
            li_tag_code = response.xpath('//div[@class="prod-feature"]/ul/li[span[@class="label" and text()="Kod produktu"]]')

            color = li_tag_color.xpath('./span[@class="value"]/text()').get() if li_tag_color.xpath('./span[@class="value"]/text()').get() else li_tag_color.xpath('./span[@class="value"]/a/text()').get()
            product_code = li_tag_code.xpath('./span[@class="value"]/text()').get()
            brand = li_tag_brand.xpath('./span[@class="value"]/a/text()').get()

            item = DetailItem()
            item["name"] = name if name is not None else ""
            item["price"] = price + ".99"
            item["product_code"] = product_code
            item["color"] = color
            item["brand"] = brand
            item["image_path_1"] = image_path_1
            item["image_path_2"] = image_path_2
            item["description"] = description if description is not None else ""

            yield item