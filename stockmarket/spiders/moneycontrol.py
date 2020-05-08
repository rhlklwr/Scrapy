# -*- coding: utf-8 -*-
import scrapy
from stockmarket.items import Stock, News


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
        top_news = response.xpath("//ul[@class='tabs_nwsconlist']/li/a")[0:5]
        market_action = response.xpath("//table[@class='rhsglTbl']/tbody")[0].xpath(".//tr")
        nse_most_active = response.xpath("//table[@class='rhsglTbl']/tbody")[2].xpath(".//tr")
        bse_most_active = response.xpath("//table[@class='rhsglTbl']/tbody")[3].xpath(".//tr")
        nse_top_gainers = response.xpath("//table[@class='rhsglTbl']/tbody")[4].xpath(".//tr")
        bse_top_gainers = response.xpath("//table[@class='rhsglTbl']/tbody")[5].xpath(".//tr")
        nse_top_losers = response.xpath("//table[@class='rhsglTbl']/tbody")[6].xpath(".//tr")
        bse_top_losers = response.xpath("//table[@class='rhsglTbl']/tbody")[7].xpath(".//tr")

        news = News()
        for entries in top_news:
            news['link'] = entries.xpath(".//@href").get()
            news['title'] = entries.xpath(".//@title").get()
            news['source'] = 'Moneycontrol'
            yield {
                'm_news': news
            }

        stock = Stock()
        for entries in nse_most_active:
            stock['name'] = entries.xpath(".//td/a/@title").get()
            stock['value'] = entries.xpath(".//td")[1].xpath(".//text()").get()
            stock['valueDifference'] = entries.xpath(".//td")[2].xpath(".//text()").get()
            # stock['value'] = entries.xpath(".//td")[3].xpath(".//text()").get()
            stock['isNegative'] = True if float(stock['valueDifference']) < 0 else False
            stock['group'] = 'MOST_ACTIVE'
            yield {
                'nse_most_active': stock
            }

        for entries in bse_most_active:
            stock['name'] = entries.xpath(".//td/a/@title").get()
            stock['value'] = entries.xpath(".//td")[1].xpath(".//text()").get()
            stock['valueDifference'] = entries.xpath(".//td")[2].xpath(".//text()").get()
            # stock['value'] = entries.xpath(".//td")[3].xpath(".//text()").get()
            stock['isNegative'] = True if float(stock['valueDifference']) < 0 else False
            stock['group'] = 'MOST_ACTIVE'
            yield {
                'bse_most_active': stock
            }

        for entries in nse_top_gainers:
            stock['name'] = entries.xpath(".//td/a/@title").get()
            stock['value'] = entries.xpath(".//td")[1].xpath(".//text()").get()
            stock['valueDifference'] = entries.xpath(".//td")[2].xpath(".//text()").get()
            stock['percentDifference'] = entries.xpath(".//td")[3].xpath(".//text()").get()
            stock['isNegative'] = True if float(stock['valueDifference']) < 0 else False
            stock['group'] = 'TOP_GAINERS'
            yield {
                'nse_top_gainers': stock
            }

        for entries in bse_top_gainers:
            stock['name'] = entries.xpath(".//td/a/@title").get()
            stock['value'] = entries.xpath(".//td")[1].xpath(".//text()").get()
            stock['valueDifference'] = entries.xpath(".//td")[2].xpath(".//text()").get()
            stock['percentDifference'] = entries.xpath(".//td")[3].xpath(".//text()").get()
            stock['isNegative'] = True if float(stock['valueDifference']) < 0 else False
            stock['group'] = 'TOP_GAINERS'
            yield {
                'bse_top_gainers': stock
            }

        for entries in nse_top_losers:
            stock['name'] = entries.xpath(".//td/a/@title").get()
            stock['value'] = entries.xpath(".//td")[1].xpath(".//text()").get()
            stock['valueDifference'] = entries.xpath(".//td")[2].xpath(".//text()").get()
            stock['percentDifference'] = entries.xpath(".//td")[3].xpath(".//text()").get()
            stock['isNegative'] = True if float(stock['valueDifference']) < 0 else False
            stock['group'] = 'TOP_LOSERS'
            yield {
                'nse_top_losers': stock
            }

        for entries in bse_top_losers:
            stock['name'] = entries.xpath(".//td/a/@title").get()
            stock['value'] = entries.xpath(".//td")[1].xpath(".//text()").get()
            stock['valueDifference'] = entries.xpath(".//td")[2].xpath(".//text()").get()
            stock['percentDifference'] = entries.xpath(".//td")[3].xpath(".//text()").get()
            stock['isNegative'] = True if float(stock['valueDifference']) < 0 else False
            stock['group'] = 'TOP_LOSERS'
            yield {
                'bse_top_losers': stock
            }

        for entries in market_action:
            stock['name'] = entries.xpath(".//td//h3/a/@title").get()
            stock['value'] = entries.xpath(".//td")[1].xpath(".//text()").get()
            stock['valueDifference'] = entries.xpath(".//td")[2].xpath(".//text()").get()
            stock['percentDifference'] = entries.xpath(".//td")[3].xpath(".//text()").get()
            stock['isNegative'] = True if float(stock['valueDifference']) < 0 else False
            stock['group'] = 'INDEX'
            yield {
                'market_action': stock
            }
