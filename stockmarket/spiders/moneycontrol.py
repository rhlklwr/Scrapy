# -*- coding: utf-8 -*-
import scrapy
from stockmarket.items import Stock, News


def news_parser(parsed_object, name):
    news = News()
    for entries in parsed_object:
        news['link'] = entries.xpath(".//@href").get()
        news['title'] = entries.xpath(".//@title").get()
        news['source'] = 'Moneycontrol'
        yield {
            name: news
        }


def stock_parser(parsed_object, name):
    stock = Stock()
    for entries in parsed_object:
        stock['name'] = entries.xpath(".//td/a/@title").get()
        stock['value'] = entries.xpath(".//td")[1].xpath(".//text()").get()
        stock['valueDifference'] = entries.xpath(".//td")[2].xpath(".//text()").get()
        if name not in ['nse_most_active', 'bse_most_active']:
            stock['percentDifference'] = entries.xpath(".//td")[3].xpath(".//text()").get()
        stock['isNegative'] = True if float(stock['valueDifference']) < 0 else False
        stock['group'] = 'MOST_ACTIVE'
        yield {
            name: stock
        }


class MoneycontrolSpider(scrapy.Spider):
    name = 'moneycontrol'
    allowed_domains = ['www.moneycontrol.com']
    # custom_settings = {
    #     'ITEM_PIPELINES': {
    #         'stockmarket.pipelines.Moneycontrol': 100
    #     }
    # }

    def start_requests(self):
        yield scrapy.Request(url='http://www.moneycontrol.com/', callback=self.parse, headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        })

    def parse(self, response):

        news_parser(response.xpath("//ul[@class='tabs_nwsconlist']/li/a")[0:5], 'm_news')
        stock_parser(response.xpath("//table[@class='rhsglTbl']/tbody")[2].xpath(".//tr"), 'nse_most_active')
        stock_parser(response.xpath("//table[@class='rhsglTbl']/tbody")[3].xpath(".//tr"), 'bse_most_active')
        stock_parser(response.xpath("//table[@class='rhsglTbl']/tbody")[4].xpath(".//tr"), 'nse_top_gainers')
        stock_parser(response.xpath("//table[@class='rhsglTbl']/tbody")[5].xpath(".//tr"), 'bse_top_gainers')
        stock_parser(response.xpath("//table[@class='rhsglTbl']/tbody")[6].xpath(".//tr"), 'nse_top_losers')
        stock_parser(response.xpath("//table[@class='rhsglTbl']/tbody")[7].xpath(".//tr"), 'bse_top_losers')
        stock_parser(response.xpath("//table[@class='rhsglTbl']/tbody")[0].xpath(".//tr"), 'market_action')



