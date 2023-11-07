import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        base_url = "https://www.centrumrowerowe.pl"
        image_url_1 = item.get('image_path_1')
        image_url_2 = item.get('image_path_2')

        print("adsasdasdadasdadadadadad")
        yield scrapy.Request(base_url + image_url_1)
        yield scrapy.Request(base_url + image_url_2)
            
    def file_path(self, request, response=None, info=None):

        filename = os.path.join("F:\\184725\\ScrapResults\\images", os.path.basename(request.url))
        print(filename)
        return filename

    def item_completed(self, results, item, info=None):

        for success, image_info in results:
            print(success, image_info)
            if success:
                if 'image_path_1' in item:
                    item['image_path_2'] = image_info['path'].split('/')[-1]
                else:
                    item['image_path_1'] = image_info['path'].split('/')[-1]
            else:
                if 'image_path_1' in item:
                    item['image_path_2'] = ""
                else:
                    item['image_path_1'] = ""
        return item