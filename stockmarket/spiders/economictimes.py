# -*- coding: utf-8 -*-
import scrapy


class EconomictimesSpider(scrapy.Spider):
    name = 'economictimes'
    allowed_domains = ['economictimes.indiatimes.com']
    start_urls = ['http://economictimes.indiatimes.com/']
    custom_settings = {
        'ITEM_PIPELINES': {
            'stockmarket.pipelines.EconomicTimes': 150
        }
    }
    def start_requests(self):
        yield scrapy.Request(url='http://economictimes.indiatimes.com/', callback=self.parse, headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        })

    def parse(self, response):
        top_news = response.xpath("////li[@data-ga-action='Widget Top News']/ul/li")[0:10]
        for idx, news in enumerate(top_news):
            link = news.xpath(".//@href").get()
            title = news.xpath(".//text()").get()
            absolute_link = response.urljoin(link)
            yield {
                "news": {
                    f"{idx + 1}": {
                        "link": absolute_link,
                        "title": title
                    }
                }
            }
