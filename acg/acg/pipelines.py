# -*- coding: utf-8 -*-

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request

# from scrapy import Request


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class AcgImagePipeline(object):
    def process_item(self, item,sqider):
        return item
class AcgPipeline(ImagesPipeline):
    headers = {
        "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
        "Accept-Encoding":" gzip, deflate",
        "Accept-Language":" en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Cache-Control":" no-cache",
        "Host":" img.gov.com.de",
        "Pragma":" no-cache",
        'referer':'',
        "Proxy-Connection":" keep-alive",
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }
    def get_meida_requests(self,item,info):
            # self.headers['Referer'] = item['url']
            # print('进入下载器')
            urls = item['image_urls']
            for image_url in urls:
                self.headers['referer'] = image_url
                yield Request(image_url, headers=self.headers)
    def item_completed(self,results, item,info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Item contains no images')
        item['image_paths'] = image_paths
        
        return item
    def file_path(self, request, response = None, info = None):
        image_guid = request.url.split('/')[-1]
        return 'full/%s'%(image_guid)
            # image_urls = item['images']
            # yield scrapy.Request(image_urls)
            # print('正在保持图片:',image_urls)
            # return item
            # for image_url in item['images']:
            
            #     print(image_url)
                # yield scrapy.Request(image_url, headers = self.headers)
    # def item_completed(self,results,item,info):
    #     print(results)
    #     image_paths = [x['path'] for ok, x in results if ok]
    #     if not image_paths:
    #         raise DropItem('没有图片')
    #     item['image_paths'] = image_paths
    #     return item

    # def item_completed(self,results, item ,info):
    #     image_paths = [x['path'] for ok ,x in results if ok]
    #     if not image_paths:
    #         raise DropItem('Item contains no images')
    #     item['image_paths'] = image_paths
