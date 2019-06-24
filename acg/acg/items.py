# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImageItem(scrapy.Item):
    url = scrapy.Field()
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()
    # define the fields for your iitem here like:
    # name = scrapy.Field()
    # title = scrapy.Field()
    # link = scrapy.Field()
    # desc = scrapy.Field()
  
