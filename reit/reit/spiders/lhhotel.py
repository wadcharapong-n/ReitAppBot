
# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from reit.items import ReitItem


class LhhotelSpider(scrapy.Spider):
    name = 'lhhotel'
    urls = ['https://www.set.or.th/set/companyprofile.do?symbol=LHHOTEL&ssoPageId=4&language=th&country=TH',
            'https://www.set.or.th/set/companyprofile.do?symbol=LHHOTEL&ssoPageId=4&language=en&country=TH',
            'https://marketdata.set.or.th/mkt/stockquotation.do?symbol=LHHOTEL&ssoPageId=1&language=th&country=TH'
            ]
    item = ReitItem()
    one = False
    two = False
    three = False

    def start_requests(self):

        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        if (response.url == self.urls[0]):
            print('Loop 0')
            # Symbol
            self.item['symbol'] = 'LHHOTEL'
            # Nickname Map To Elasticsearch
            self.item['nickName'] = 'โรงแรมแกรนด์เซนเตอร์พอยต์เทอร์มินอล 21 โรงแรมแกรนด์เซนเตอร์พอยต์เทอร์มินอล โรงแรมแกรนด์ เซนเตอร์พอยต์ เทอร์มินอล 21 Grand Center Point Terminal 21 Hotel โรงแรมแกรนด์เซนเตอร์พอยต์ราชดำริ โรงแรมแกรนด์ เซนเตอร์พอยต์ '
            # Trustee Map To Elasticsearch
            self.item['trustee'] = 'บริษัทหลักทรัพย์จัดการกองทุน ไทยพาณิชย์ จำกัด'
            # Trust Name TH
            self.item['trustNameTh'] = response.css(
                "tr td div.row div.col-md-9::text").getall()[0].strip()
            # Address
            self.item['address'] = response.css(
                "tr td div.row div.col-md-9::text").getall()[1].strip()
            # Url
            self.item['url'] = response.css(
                "td div.row div.col-xs-12 a::text").getall()[0].strip()
            # Reit Manager
            self.item['reitManager'] = response.css(
                "tr td div.row div.col-md-9::text").getall()[4].strip()
            # Property Manager
            self.item['propertyManager'] = response.css(
                "tr td div.row div.col-md-9::text").getall()[5].strip()
            # Investment Policy
            self.item['investmentPolicy'] = response.css(
                "tr td div.row div.col-md-9::text").getall()[6].strip()
            # Pe Value
            self.item['peValue'] = response.css(
                "td div.row div.col-xs-12 div::text").getall()[1].strip()
            # Par/NAV
            self.item['parNAV'] = response.css(
                "td div.row div.col-xs-12 div::text").getall()[5].strip()
            # Dvd/Yield
            self.item['dvdYield'] = response.css(
                "td div.row div.col-xs-12 div::text").getall()[3].strip()
            # Investment Amount
            self.item['investmentAmount'] = response.css(
                "td div.row div.col-xs-9::text").getall()[9].strip()
            # Policy
            self.item['policy'] = response.css(
                "td div.row div.col-xs-12::text").getall()[60].strip()
            # Establishment Date
            self.item['establishmentDate'] = '11/12/2015'
            # Registration Date
            self.item['registrationDate'] = '22/12/2558'

            self.one = True

        if (response.url == self.urls[1]):
            print('Loop 1')
            # Trust Name TH
            self.item['trustNameEn'] = response.css(
                "tr td div.row div.col-md-9::text").getall()[0].strip()

            self.two = True

        if (response.url == self.urls[2]):
            print('Loop 2')
            # Price of Day
            price_of_day = response.css("tbody")[0].css("tr")[
                1].css("td::text").getall()
            if len(price_of_day) == 2:
                self.item['priceOfDay'] = response.css("tbody")[0].css("tr")[
                    1].css("td::text")[1].get().strip()
            elif len(price_of_day) == 3:
                self.item['priceOfDay'] = response.css("tbody")[0].css("tr")[
                    1].css("td::text")[2].get().strip()
            # Max Price of Day
            self.item['maxPriceOfDay'] = response.css("tbody")[0].css("tr")[
                6].css('td::text')[1].get().strip()
            # Min Price of Day
            self.item['minPriceOfDay'] = response.css("tbody")[0].css("tr")[
                7].css('td::text')[1].get().strip()
            # Par Value
            self.item['parValue'] = response.css("tbody")[1].css("tr")[
                0].css("td::text")[1].get().strip()
            # Ceiling Value
            self.item['ceilingValue'] = response.css("tbody")[1].css("tr")[
                1].css("td::text")[1].get().strip()
            # Foor Value
            self.item['floorValue'] = response.css("tbody")[1].css("tr")[
                2].css("td::text")[1].get().strip()

            self.three = True

        print("End Loop")
        if (self.one == True) and (self.two == True) and (self.three == True):
            yield self.item
