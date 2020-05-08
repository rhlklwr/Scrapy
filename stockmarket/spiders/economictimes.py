# -*- coding: utf-8 -*-
import scrapy
from stockmarket.items import News

class EconomictimesSpider(scrapy.Spider):
    name = 'economictimes'
    allowed_domains = ['economictimes.indiatimes.com']
    start_urls = ['http://economictimes.indiatimes.com/']
    # custom_settings = {
    #     'ITEM_PIPELINES': {
    #         'stockmarket.pipelines.EconomicTimes': 150
    #     }
    # }
    def start_requests(self):
        yield scrapy.Request(url='http://economictimes.indiatimes.com/', callback=self.parse, headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        })

    def parse(self, response):
        top_news = response.xpath("////li[@data-ga-action='Widget Top News']/ul/li")[0:10]
        news = News()
        for idx, entries in top_news:
            link = entries.xpath(".//@href").get()
            news['title'] = entries.xpath(".//text()").get()
            news['link'] = response.urljoin(link)
            news['source'] = 'economictimes'
            yield {
                'e_news': news
            }
