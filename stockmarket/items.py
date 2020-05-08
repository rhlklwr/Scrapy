# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Stock(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    value = scrapy.Field()
    valueDifference = scrapy.Field()
    percentDifference = scrapy.Field()
    isNegative = scrapy.Field()
    group = scrapy.Field()


class News(scrapy.Item):
    id = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    source = scrapy.Field()