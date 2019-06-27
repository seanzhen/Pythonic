# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EarthquakeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    level = scrapy.Field()

    o_time = scrapy.Field()

    latitude = scrapy.Field()

    longitude = scrapy.Field()

    depth = scrapy.Field()

    location = scrapy.Field()

    
