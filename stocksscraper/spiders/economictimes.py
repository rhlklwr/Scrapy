# -*- coding: utf-8 -*-
import scrapy


class EconomictimesSpider(scrapy.Spider):
    name = 'economictimes'
    allowed_domains = ['economictimes.indiatimes.com']
    start_urls = ['http://economictimes.indiatimes.com/']

    def parse(self, response):
        pass
