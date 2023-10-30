class DetailSpider(scrapy.Spider):
    name = 'deatil_spider'

    def start_requests(self):


        base_url = "https://www.centrumrowerowe.pl/"

        for i in range(len(categories)):
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
