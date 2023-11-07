import scrapy

class ListItem(scrapy.Item):
    product_site_path = scrapy.Field()

class DetailItem(scrapy.Item):
    name = scrapy.Field()
    image_path_1 = scrapy.Field()
    image_path_2 = scrapy.Field()
    price = scrapy.Field()
    brand = scrapy.Field()
    product_code = scrapy.Field()
    description = scrapy.Field()
    color = scrapy.Field()
