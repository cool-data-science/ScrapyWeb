# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings


class DramaPipeline(object):
    
    def __init__(self):
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=int(settings['MONGO_PORT']))
        self.db = self.client[settings['MONGO_DB']]
        
    def process_item(self, item, spider):
        #postItem = dict(item.load_item)
        self.db['drama'].insert_many(item)
        return item
        