# -*- coding: utf-8 -*-

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import requests
# from scrapy import Request


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AcgPipeline(ImagesPipeline):
    headers = {
        "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
        "Accept-Encoding":" gzip, deflate",
        "Accept-Language":" en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Cache-Control":" no-cache",
        "Host":" img.gov.com.de",
        "Pragma":" no-cache",
        "Proxy-Connection":" keep-alive",
        "User-Agent":" Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36"
    }
    def get_meida_requests(self,item,info):
            self.headers['Referer'] = item['url']
            for image_url in item['images']:
                print(image_url)
                # yield scrapy.Request(image_url, headers = self.headers)
                requests.get(image_url)
                print('正在保存图片')
    # def item_completed(self,results, item ,info):
    #     image_paths = [x['path'] for ok ,x in results if ok]
    #     if not image_paths:
    #         raise DropItem('Item contains no images')
    #     item['image_paths'] = image_paths
    #     return item
