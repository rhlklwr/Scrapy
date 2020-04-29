# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from utils.firestore_database import FirestoreDatabase


class Moneycontrol(object):

    def process_item(self, item, spider):

        with FirestoreDatabase() as db:
            if 'news' in dict(item):
                top_news = db.collection(u'News').document(u'Moneycontrol')
                db.batch.update(top_news, dict(item)['news'])
            if 'nse_most_active' in dict(item):
                nse_most_active = db.collection(u'nse').document(u'most_active')
                db.batch.update(nse_most_active, dict(item)['nse_most_active'])
            if 'bse_most_active' in dict(item):
                bse_most_active = db.collection(u'bse').document(u'most_active')
                db.batch.update(bse_most_active, dict(item)['bse_most_active'])
            if 'nse_top_gainers' in dict(item):
                nse_top_gainers = db.collection(u'nse').document(u'top_gainers')
                db.batch.update(nse_top_gainers, dict(item)['nse_top_gainers'])
            if 'bse_top_gainers' in dict(item):
                bse_top_gainers = db.collection(u'bse').document(u'top_gainers')
                db.batch.update(bse_top_gainers, dict(item)['bse_top_gainers'])
            if 'nse_top_losers' in dict(item):
                nse_top_losers = db.collection(u'nse').document(u'top_losers')
                db.batch.update(nse_top_losers, dict(item)['nse_top_losers'])
            if 'bse_top_losers' in dict(item):
                bse_top_losers = db.collection(u'bse').document(u'top_losers')
                db.batch.update(bse_top_losers, dict(item)['bse_top_losers'])
            if 'market_action_index' in dict(item):
                market_action = db.collection(u'Market_Index').document(u'Indexes')
                db.batch.update(market_action, dict(item)['market_action_index'])
            return item


class EconomicTimes(object):

    def process_item(self, item, spider):

        with FirestoreDatabase as db:
            if 'news' in dict(item):
                top_news = db.collection(u'News').document(u'EconomicTimes')
                db.batch().update(top_news, dict(item)['news'])
            return item