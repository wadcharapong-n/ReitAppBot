
# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from majorshareholder.items import MajorshareholderItem


class BofficeSpider(scrapy.Spider):
    name = 'boffice'
    urls = ['https://www.set.or.th/set/companyholder.do?symbol=boffice&ssoPageId=6&language=th&country=TH']

    item = {}
    item[0] = MajorshareholderItem()
    item[1] = MajorshareholderItem()
    item[2] = MajorshareholderItem()
    item[3] = MajorshareholderItem()
    item[4] = MajorshareholderItem()

    def start_requests(self):

        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.item[0]['symbol'] = 'BOFFICE'
        self.item[0]['nameTh'] = response.css("tbody tr td::text").getall()[1].strip()
        self.item[0]['nameEn'] = ''
        self.item[0]['shares'] = response.css("tbody tr td::text").getall()[2].strip()
        self.item[0]['sharesPercent'] = response.css(
            "tbody tr td::text").getall()[3].strip()

        self.item[1]['symbol'] = 'BOFFICE'
        self.item[1]['nameTh'] = response.css("tbody tr td::text").getall()[5].strip()
        self.item[1]['nameEn'] = ''
        self.item[1]['shares'] = response.css("tbody tr td::text").getall()[6].strip()
        self.item[1]['sharesPercent'] = response.css(
            "tbody tr td::text").getall()[7].strip()

        self.item[2]['symbol'] = 'BOFFICE'
        self.item[2]['nameTh'] = response.css("tbody tr td::text").getall()[9].strip()
        self.item[2]['nameEn'] = ''
        self.item[2]['shares'] = response.css("tbody tr td::text").getall()[10].strip()
        self.item[2]['sharesPercent'] = response.css(
            "tbody tr td::text").getall()[11].strip()

        self.item[3]['symbol'] = 'BOFFICE'
        self.item[3]['nameTh'] = response.css(
            "tbody tr td::text").getall()[13].strip()
        self.item[3]['nameEn'] = ''
        self.item[3]['shares'] = response.css("tbody tr td::text").getall()[14].strip()
        self.item[3]['sharesPercent'] = response.css(
            "tbody tr td::text").getall()[15].strip()

        self.item[4]['symbol'] = 'BOFFICE'
        self.item[4]['nameTh'] = response.css(
            "tbody tr td::text").getall()[17].strip()
        self.item[4]['nameEn'] = ''
        self.item[4]['shares'] = response.css("tbody tr td::text").getall()[18].strip()
        self.item[4]['sharesPercent'] = response.css(
            "tbody tr td::text").getall()[19].strip()

        yield self.item
