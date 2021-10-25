# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

# Instantiate Firestore class
default_db = firestore.client()


class Moneycontrol(object):

    def open_spider(self, spider, db=default_db):
        self.db = db
        # Instantiate batch class to update data in single batch
        self.batch = self.db.batch()

    def close_spider(self, spider):
        self.batch.commit()

    def process_item(self, item, spider):
        news = self.db.collection(u'news').document()
        nse = self.db.collection(u'nse').document()
        bse = self.db.collection(u'bse').document()
        market = self.db.collection(u'market').document()

        if 'm_news' in item:
            news.set(item['m_news'])
        if 'nse_most_active' in item:
            self.batch.update(nse, item['nse_most_active'])
        if 'bse_most_active' in item:
            self.batch.update(bse, item['bse_most_active'])
        if 'nse_top_gainers' in item:
            self.batch.set(nse, item['nse_top_gainers'])
        if 'bse_top_gainers' in item:
            self.batch.set(bse, item['bse_top_gainers'])
        if 'nse_top_losers' in item:
            self.batch.set(nse, item['nse_top_losers'])
        if 'bse_top_losers' in item:
            self.batch.set(bse, item['bse_top_losers'])
        if 'market_action' in item:
            self.batch.set(market, item['market_action'])

        return item


class EconomicTimes(object):

    def open_spider(self, spider, db=default_db):
        self.db = db
        # Instantiate batch class to update data in single batch
        self.batch = self.db.batch()

    def close_spider(self, spider):
        self.batch.commit()

    def process_item(self, item, spider):
        news = self.db.collection(u'news').document()
        if 'e_news' in item:
            self.batch.update(news, item['e_news'])

        return item