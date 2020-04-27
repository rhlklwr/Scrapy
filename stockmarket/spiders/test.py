# -*- coding: utf-8 -*-

"""
Failed
"""
import scrapy
from stockmarket.items import *


class MoneycontrolSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.moneycontrol.com']
    urls = 'http://www.moneycontrol.com'

    def start_requests(self):
        yield scrapy.Request(url=MoneycontrolSpider.urls, callback=self.news, headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                           (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        })

    def news(self, response):
        top_news = response.xpath("//ul[@class='tabs_nwsconlist']/li/a")[0:5]
        news_item = NewsItem()
        for idx, news in enumerate(top_news):
            news_item['num'] = f"{idx + 1}"
            news_item['link'] = news.xpath(".//@href").get()
            news_item['title'] = news.xpath(".//@title").get()
            yield response.follow(url=MoneycontrolSpider.urls, callback=self.most_active_nse,
                                  meta={'News_dict': news_item})

    def most_active_nse(self, response):
        most_active = NseMostActive()
        nse_most_active = response.xpath("//table[@class='rhsglTbl']/tbody")[2].xpath(".//tr")
        nse_most_active_companies = nse_most_active.xpath(".//td/a/@title")
        for idx, companies, entries in zip(range(1, 6), nse_most_active_companies, nse_most_active):
            most_active['nse_most_active'] = f"{idx}"
            most_active['Company'] = companies.get()
            most_active['Price'] = entries.xpath(".//td")[1].xpath(".//text()").get()
            most_active['Change'] = entries.xpath(".//td")[2].xpath(".//text()").get()
            most_active['Value'] = entries.xpath(".//td")[3].xpath(".//text()").get()
            yield response.follow(url=MoneycontrolSpider.urls, callback=self.most_active_bse,
                                  meta={'News_dict': response.request.meta['News_dict'],
                                        "most_active_nse_dict": most_active})

    def most_active_bse(self, response):
        most_active = BseMostActive()
        bse_most_active = response.xpath("//table[@class='rhsglTbl']/tbody")[3].xpath(".//tr")
        bse_most_active_companies = bse_most_active.xpath(".//td/a/@title")
        for idx, companies, entries in zip(range(1, 6), bse_most_active_companies, bse_most_active):
            most_active['bse_most_active'] = f"{idx}"
            most_active['Company'] = companies.get()
            most_active['Price'] = entries.xpath(".//td")[1].xpath(".//text()").get()
            most_active['Change'] = entries.xpath(".//td")[2].xpath(".//text()").get()
            most_active['Value'] = entries.xpath(".//td")[3].xpath(".//text()").get()
            yield response.follow(url=MoneycontrolSpider.urls, callback=self.top_gainers_nse,
                                  meta={'News_dict': response.request.meta['News_dict'],
                                        'most_active_nse_dict': response.request.meta['most_active_nse_dict'],
                                        "most_active_bse_dict": most_active})

    def top_gainers_nse(self, response):
        top_gainers = NseTopGainers()
        nse_top_gainers = response.xpath("//table[@class='rhsglTbl']/tbody")[4].xpath(".//tr")
        nse_top_gainers_companies = nse_top_gainers.xpath(".//td/a/@title")
        for idx, companies, entries in zip(range(1, 6), nse_top_gainers_companies, nse_top_gainers):
            top_gainers['nse_top_gainers'] = f"{idx}"
            top_gainers['Company'] = companies.get()
            top_gainers['Price'] = entries.xpath(".//td")[1].xpath(".//text()").get()
            top_gainers['Change'] = entries.xpath(".//td")[2].xpath(".//text()").get()
            top_gainers['Gain'] = entries.xpath(".//td")[3].xpath(".//text()").get()
            yield response.follow(url=MoneycontrolSpider.urls, callback=self.top_gainers_bse,
                                  meta={'News_dict': response.request.meta['News_dict'],
                                        'most_active_nse_dict': response.request.meta['most_active_nse_dict'],
                                        'most_active_bse_dict': response.request.meta['most_active_bse_dict'],
                                        "top_gainers_nse_dict": top_gainers})

    def top_gainers_bse(self, response):
        top_gainers = BseTopGainers()
        bse_top_gainers = response.xpath("//table[@class='rhsglTbl']/tbody")[5].xpath(".//tr")
        bse_top_gainers_companies = bse_top_gainers.xpath(".//td/a/@title")
        for idx, companies, entries in zip(range(1, 6), bse_top_gainers_companies, bse_top_gainers):
            top_gainers['bse_top_gainers'] = f"{idx}"
            top_gainers['Company'] = companies.get()
            top_gainers['Price'] = entries.xpath(".//td")[1].xpath(".//text()").get()
            top_gainers['Change'] = entries.xpath(".//td")[2].xpath(".//text()").get()
            top_gainers['Gain'] = entries.xpath(".//td")[3].xpath(".//text()").get()
            yield response.follow(url=MoneycontrolSpider.urls, callback=self.top_looser_nse,
                                  meta={'News_dict': response.request.meta['News_dict'],
                                        'most_active_nse_dict': response.request.meta['most_active_nse_dict'],
                                        'most_active_bse_dict': response.request.meta['most_active_bse_dict'],
                                        'top_gainers_nse_dict': response.request.meta['top_gainers_nse_dict'],
                                        "top_gainers_bse_dict": top_gainers})

    def top_looser_nse(self, response):
        top_looser = NseTopLosers()
        nse_top_losers = response.xpath("//table[@class='rhsglTbl']/tbody")[6].xpath(".//tr")
        nse_top_losers_companies = nse_top_losers.xpath(".//td/a/@title")
        for idx, companies, entries in zip(range(1, 6), nse_top_losers_companies, nse_top_losers):
            top_looser['nse_top_losers'] = f"{idx}"
            top_looser['Company'] = companies.get()
            top_looser['Price'] = entries.xpath(".//td")[1].xpath(".//text()").get()
            top_looser['Change'] = entries.xpath(".//td")[2].xpath(".//text()").get()
            top_looser['Loss'] = entries.xpath(".//td")[3].xpath(".//text()").get()
            yield response.follow(url=MoneycontrolSpider.urls, callback=self.top_looser_bse,
                                  meta={'News_dict': response.request.meta['News_dict'],
                                        'most_active_nse_dict': response.request.meta['most_active_nse_dict'],
                                        'most_active_bse_dict': response.request.meta['most_active_bse_dict'],
                                        'top_gainers_nse_dict': response.request.meta['top_gainers_nse_dict'],
                                        'top_gainers_bse_dict': response.request.meta['top_gainers_bse_dict'],
                                        "top_looser_nse_dict": top_looser})

    def top_looser_bse(self, response):
        top_looser = BseTopLosers()
        bse_top_losers = response.xpath("//table[@class='rhsglTbl']/tbody")[7].xpath(".//tr")
        bse_top_losers_companies = bse_top_losers.xpath(".//td/a/@title")
        for idx, companies, entries in zip(range(1, 6), bse_top_losers_companies, bse_top_losers):
            top_looser['bse_top_losers'] = f"{idx}"
            top_looser['Company'] = companies.get()
            top_looser['Price'] = entries.xpath(".//td")[1].xpath(".//text()").get()
            top_looser['Change'] = entries.xpath(".//td")[2].xpath(".//text()").get()
            top_looser['Loss'] = entries.xpath(".//td")[3].xpath(".//text()").get()
            yield response.follow(url=MoneycontrolSpider.urls, callback=self.market_action_index,
                                  meta={'News_dict': response.request.meta['News_dict'],
                                        'most_active_nse_dict': response.request.meta['most_active_nse_dict'],
                                        'most_active_bse_dict': response.request.meta['most_active_bse_dict'],
                                        'top_gainers_nse_dict': response.request.meta['top_gainers_nse_dict'],
                                        'top_gainers_bse_dict': response.request.meta['top_gainers_bse_dict'],
                                        'top_looser_nse_dict': response.request.meta['top_looser_nse_dict'],
                                        "top_looser_bse_dict": top_looser})

    def market_action_index(self, response):
        market = MarketAction()
        market_action = response.xpath("//table[@class='rhsglTbl']/tbody")[0].xpath(".//tr")
        market_action_index = market_action.xpath(".//td//h3/a/@title")
        for idx, indexes, entries in zip(range(1, 6), market_action_index, market_action):
            market['market_action_index'] = f"{idx}"
            market['Index'] = indexes.get()
            market['Price'] = entries.xpath(".//td")[1].xpath(".//text()").get()
            market['Change'] = entries.xpath(".//td")[2].xpath(".//text()").get()
            market['percentage_Change'] = entries.xpath(".//td")[3].xpath(".//text()").get()
            yield{
                'News_dict': response.request.meta['News_dict'],
                'most_active_nse_dict': response.request.meta['most_active_nse_dict'],
                'most_active_bse_dict': response.request.meta['most_active_bse_dict'],
                'top_gainers_nse_dict': response.request.meta['top_gainers_nse_dict'],
                'top_gainers_bse_dict': response.request.meta['top_gainers_bse_dict'],
                'top_looser_nse_dict': response.request.meta['top_looser_nse_dict'],
                'top_looser_bse_dict': response.request.meta['top_looser_bse_dict'],
                'market_action_dict': market
                }