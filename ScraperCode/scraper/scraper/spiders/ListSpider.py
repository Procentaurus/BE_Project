import scrapy
from ..items import ListItem

class ListSpider(scrapy.Spider):

    name = "list_spider"

    custom_settings = {
        'FEEDS': { 'C:\\PG\\sem_5\\BE\\Project\\ScrapResults\\data.csv': {
            'format': 'csv',
            'overwrite': True,
            'encoding': 'utf8',
            'csv_delimiter': ';'
        }}
    }

    def start_requests(self):

        categories = ["warsztat-rowerowy", "akcesoria", "czesci", "odziez-rowerowa"]
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

        for i in range(len(categories)):
            for j in range(len(sub_categories[0])):
                for k in range(1,11):
                    url = "{}/{}/{}/?page={}".format(base_url, categories[i], sub_categories[i][j], k)
                    yield scrapy.Request(url, callback=self.parse, cb_kwargs={'sub_category': sub_categories_pl[i][j]})

    def parse(self, response, sub_category):

        body_element = response.css('body')
        body_class = body_element.css('::attr(class)').get()

        if body_class != "notFound":

            # Retrieving needed elements
            a_tags = response.xpath('//div[@class="photo"]/a[img]')

            a_tags_hrefs = [a_tag.css('::attr(href)').extract() for a_tag in a_tags]

            for product_path in a_tags_hrefs:
                item = ListItem()
                item['product_site_path'] = product_path
                item['sub_category'] = sub_category
                yield item