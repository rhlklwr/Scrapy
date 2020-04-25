# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import firebase_admin
from firebase_admin import credentials, firestore


class FireStore(object):

    def open_spider(self, spider):
        # Authentication with Firebase
        self.cred = credentials.Certificate("./ServiceAccountKey.json")
        self.app = firebase_admin.initialize_app(self.cred)

        # Instantiate Firestore class
        self.db = firestore.client()

        # Instantiate batch class to update data in single batch
        self.batch = self.db.batch()

    def close_spider(self, spider):
        self.batch.commit()

    def process_item(self, item, spider):
        top_news = self.db.collection(u'News').document(u'Moneycontrol')
        market_action = self.db.collection(u'Market_Index').document(u'Indexes')
        nse_most_active = self.db.collection(u'nse').document(u'most_active')
        bse_most_active = self.db.collection(u'bse').document(u'most_active')
        nse_top_gainers = self.db.collection(u'nse').document(u'top_gainers')
        bse_top_gainers = self.db.collection(u'bse').document(u'top_gainers')
        nse_top_losers = self.db.collection(u'nse').document(u'top_losers')
        bse_top_losers = self.db.collection(u'bse').document(u'top_losers')

        self.batch.update(top_news, item['news'])
        # self.batch.update(market_action, item["market_action_index"])
        # self.batch.update(nse_most_active, dict(item)["nse_most_active"])
        # self.batch.update(bse_most_active, dict(item)["bse_most_active"])
        # self.batch.update(nse_top_gainers, dict(item)["nse_top_gainers"])
        # self.batch.update(bse_top_gainers, dict(item)["bse_top_gainers"])
        # self.batch.update(nse_top_losers, dict(item)["nse_top_losers"])
        # self.batch.update(bse_top_losers, dict(item)["bse_top_losers"])

        return item
