import scrapy

class ListItem(scrapy.Item):
    product_site_path = scrapy.Field()
    sub_category = scrapy.Field()

class ProductItem(scrapy.Item):
    Product_ID = scrapy.Field()
    Active = scrapy.Field()
    Name = scrapy.Field()
    Wholesale_price = scrapy.Field()
    Weight = scrapy.Field()
    Delivery_time_of_in_stock_products = scrapy.Field()
    Quantity = scrapy.Field()
    Description = scrapy.Field()
    Available_for_order = scrapy.Field()
    Image_URLs = scrapy.Field()
    Manufacturer = scrapy.Field()
    Categories = scrapy.Field()
    Color = scrapy.Field()


class CategoryItem(scrapy.Item):
    Category_ID = scrapy.Field()
    Active = scrapy.Field()
    Name = scrapy.Field()
    Parent_category = scrapy.Field()
    Root_category = scrapy.Field()
    
