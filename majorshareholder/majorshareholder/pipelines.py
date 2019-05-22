# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


class MajorshareholderPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for index in item:
            for data in item[index]:
                if not data:
                    valid = False
                    raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.remove({'symbol': item[index]['symbol']})
            for index in item:
                self.collection.insert(dict(item[index]))
                log.msg("Majorshareholder Create In MongoDB",
                        level=log.DEBUG, spider=spider)
        else:
            log.msg("Majorshareholder Invalid Data",
                    level=log.DEBUG, spider=spider)

        return item
