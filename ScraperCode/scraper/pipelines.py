import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        base_url = "https://www.centrumrowerowe.pl"
        image_url = item.get('image_path')
        if image_url:
            yield scrapy.Request(base_url + image_url)
            
    def file_path(self, request, response=None, info=None):
        script_folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        download_folder = script_folder + "\\ScrapResults\\{}".format("smallImages")
        filename = os.path.join(download_folder, os.path.basename(request.url))

        return filename

    def item_completed(self, results, item, info=None):
        for success, image_info in results:
            if success:

                last_two_parts = image_info['path'].split('\\')[-2:]
                item['image_path'] = os.path.join(*last_two_parts)
                return item
