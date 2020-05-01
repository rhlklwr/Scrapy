# -*- coding: utf-8 -*-
import scrapy


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
        market_action_index = market_action.xpath(".//td//h3/a/@title")
        nse_most_active = response.xpath("//table[@class='rhsglTbl']/tbody")[2].xpath(".//tr")
        nse_most_active_companies = nse_most_active.xpath(".//td/a/@title")
        bse_most_active = response.xpath("//table[@class='rhsglTbl']/tbody")[3].xpath(".//tr")
        bse_most_active_companies = bse_most_active.xpath(".//td/a/@title")
        nse_top_gainers = response.xpath("//table[@class='rhsglTbl']/tbody")[4].xpath(".//tr")
        nse_top_gainers_companies = nse_top_gainers.xpath(".//td/a/@title")
        bse_top_gainers = response.xpath("//table[@class='rhsglTbl']/tbody")[5].xpath(".//tr")
        bse_top_gainers_companies = bse_top_gainers.xpath(".//td/a/@title")
        nse_top_losers = response.xpath("//table[@class='rhsglTbl']/tbody")[6].xpath(".//tr")
        nse_top_losers_companies = nse_top_losers.xpath(".//td/a/@title")
        bse_top_losers = response.xpath("//table[@class='rhsglTbl']/tbody")[7].xpath(".//tr")
        bse_top_losers_companies = bse_top_losers.xpath(".//td/a/@title")

        for idx, news in enumerate(top_news):
            link = news.xpath(".//@href").get()
            title = news.xpath(".//@title").get()
            yield {
                "m_news": {
                    f"{idx + 1}": {
                        "link": link,
                        "title": title
                    }
                }
            }
        for idx, companies, entries in zip(range(1, 6), nse_most_active_companies, nse_most_active):
            company_name = companies.get()
            price = entries.xpath(".//td")[1].xpath(".//text()").get()
            change = entries.xpath(".//td")[2].xpath(".//text()").get()
            value = entries.xpath(".//td")[3].xpath(".//text()").get()
            yield {
                "nse_most_active": {
                    f"{idx}": {
                        "Company": company_name,
                        "Price": price,
                        "Change": change,
                        "Value": value
                    }
                }
            }

        for idx, companies, entries in zip(range(1, 6), bse_most_active_companies, bse_most_active):
            company_name = companies.get()
            price = entries.xpath(".//td")[1].xpath(".//text()").get()
            change = entries.xpath(".//td")[2].xpath(".//text()").get()
            value = entries.xpath(".//td")[3].xpath(".//text()").get()
            yield {
                "bse_most_active": {
                    f"{idx}": {
                        "Company": company_name,
                        "Price": price,
                        "Change": change,
                        "Value": value
                    }
                }
            }
        for idx, companies, entries in zip(range(1, 6), nse_top_gainers_companies, nse_top_gainers):
            company_name = companies.get()
            price = entries.xpath(".//td")[1].xpath(".//text()").get()
            change = entries.xpath(".//td")[2].xpath(".//text()").get()
            gain = entries.xpath(".//td")[3].xpath(".//text()").get()
            yield {
                "nse_top_gainers": {
                    f"{idx}": {
                        "Company": company_name,
                        "Price": price,
                        "Change": change,
                        "%Gain": gain
                    }
                }
            }
        for idx, companies, entries in zip(range(1, 6), bse_top_gainers_companies, bse_top_gainers):
            company_name = companies.get()
            price = entries.xpath(".//td")[1].xpath(".//text()").get()
            change = entries.xpath(".//td")[2].xpath(".//text()").get()
            gain = entries.xpath(".//td")[3].xpath(".//text()").get()
            yield {
                "bse_top_gainers": {
                    f"{idx}": {
                        "Company": company_name,
                        "Price": price,
                        "Change": change,
                        "%Gain": gain
                    }
                }
            }
        for idx, companies, entries in zip(range(1, 6), nse_top_losers_companies, nse_top_losers):
            company_name = companies.get()
            price = entries.xpath(".//td")[1].xpath(".//text()").get()
            change = entries.xpath(".//td")[2].xpath(".//text()").get()
            loss = entries.xpath(".//td")[3].xpath(".//text()").get()
            yield {
                "nse_top_losers": {
                    f"{idx}": {
                        "Company": company_name,
                        "Price": price,
                        "Change": change,
                        "%Loss": loss
                    }
                }
            }
        for idx, companies, entries in zip(range(1, 6), bse_top_losers_companies, bse_top_losers):
            company_name = companies.get()
            price = entries.xpath(".//td")[1].xpath(".//text()").get()
            change = entries.xpath(".//td")[2].xpath(".//text()").get()
            loss = entries.xpath(".//td")[3].xpath(".//text()").get()
            yield {
                "bse_top_losers": {
                    f"{idx}": {
                        "Company": company_name,
                        "Price": price,
                        "Change": change,
                        "%Loss": loss
                    }
                }
            }
        for idx, indexes, entries in zip(range(1, 6), market_action_index, market_action):
            index = indexes.get()
            price = entries.xpath(".//td")[1].xpath(".//text()").get()
            change = entries.xpath(".//td")[2].xpath(".//text()").get()
            percent_change = entries.xpath(".//td")[3].xpath(".//text()").get()
            yield {
                "market_action_index": {
                    f"{idx}": {
                        "Index": index,
                        "Price": price,
                        "Change": change,
                        "%Change": percent_change
                    }
                }
            }