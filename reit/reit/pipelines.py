# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


class ReitPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            if self.checkDuplicate(item, spider):
                # Check Update Field
                log.msg("Check Duplicate",
                        level=log.DEBUG, spider=spider)
                dataInMongo = self.findDataInMongo(item, spider)
                for key in dataInMongo:
                    if key != '_id':
                        if dataInMongo[key] != item[key]:
                            myquery = {key: dataInMongo[key]}
                            newvalues = {"$set": {key: item[key]}}
                            self.collection.update_one(myquery, newvalues)
                            log.msg("REIT Updated Data In MongoDB",
                                    level=log.DEBUG, spider=spider)
            else:
                self.collection.insert(dict(item))
                log.msg("REIT Create In MongoDB",
                        level=log.DEBUG, spider=spider)
        else:
            log.msg("REIT Invalid Data",
                    level=log.DEBUG, spider=spider)

        return item

    def checkDuplicate(self, item, spider):
        data = self.findDataInMongo(item, spider)
        if data is not None:
            return True

        return False

    def findDataInMongo(self, item, spider):
        item_db = self.collection.find({'symbol': item['symbol']})
        for data in item_db:
            if data['symbol'] == item['symbol']:
                return data

        return None
