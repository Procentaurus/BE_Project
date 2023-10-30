import scrapy
from ..items import DetailItem
import os
import csv

class DetailSpider(scrapy.Spider):
    name = 'detail_spider'

    def start_requests(self):

        with open()
        site_urls = 
        base_url = "https://www.centrumrowerowe.pl/"

        for i in range(len(categories)):
            for j in range(len(sub_categories[0])):
                for k in range(1,12):
                    url = "{}/{}/{}/?page={}".format(base_url, categories[i], sub_categories[i][j], k)
                    yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):

        body_element = response.css('body')
        body_class = body_element.css('::attr(class)').get()

        if body_class != "notFound":

            # Retrieving needed elements
            a_tags = response.xpath('//div[@class="photo"]/a[img]')


            a_tags_hrefs = [a_tag.css('::attr(href)').extract() for a_tag in a_tags]
            img_tags_in_a_tags = [a_tag.css('img[data-default^="/photo/product"][data-default$="w280-h280.png"]') for a_tag in a_tags]

            img_urls = [url for img_tag in img_tags_in_a_tags for url in img_tag.css('::attr(data-default)').extract()]

            # Ascribe evry item with data about paths
            data = []
            for image_url, product_path in zip(img_urls, a_tags_hrefs):
                item = ListItem()
                item['image_path'] = image_url
                item['product_site_path'] = product_path

                data.append({
                    "image_path": item['image_path'].split('/')[-1],
                    "site_path": item['product_site_path'][0]
                })
                yield item
    
            self.save_to_csv(data)

    def save_to_csv(self, data):

        flag = os.path.exists('C:\\PG\\sem_5\\BE\\Project\\ScrapResults\\data.csv')

        with open('C:\\PG\\sem_5\\BE\\Project\\ScrapResults\\data.csv', 'a', newline='') as csvfile:
            fieldnames = ['image_path', 'site_path']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not flag:
                writer.writeheader()
                
            for data_entry in data:
                writer.writerow(data_entry)