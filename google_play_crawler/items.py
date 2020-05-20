# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class GooglePlayCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    Name = scrapy.Field()
    Link = scrapy.Field()
    LastUpdated = scrapy.Field()
    Author = scrapy.Field()
    Filesize = scrapy.Field()
    Installs = scrapy.Field()
    Version = scrapy.Field()
    Compatibility = scrapy.Field()
    ContentRating = scrapy.Field()
    Genre = scrapy.Field()
    Price = scrapy.Field()
    RatingValue = scrapy.Field()
    ReviewNumber = scrapy.Field()
    pass
