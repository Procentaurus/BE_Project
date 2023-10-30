import scrapy

class ListItem(scrapy.Item):
    image_path = scrapy.Field()
    product_site_path = scrapy.Field()

class DetailItem(scrapy.Item):
    name = scrapy.Field()
    large_image_path = scrapy.Field()
    small_image_path = scrapy.Field()
    price = scrapy.Field()
    brand = scrapy.Field()
    product_code = scrapy.Field()
    description = scrapy.Field()
