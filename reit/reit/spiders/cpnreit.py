
# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from reit.items import ReitItem


class CpnreitSpider(scrapy.Spider):
    name = 'cpnreit'
    urls = ['https://www.set.or.th/set/companyprofile.do?symbol=CPNREIT&language=th&country=TH',
            'https://www.set.or.th/set/companyprofile.do?symbol=CPNREIT&language=en&country=TH',
            'https://marketdata.set.or.th/mkt/stockquotation.do?symbol=CPNREIT&ssoPageId=1&language=th&country=TH'
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
            self.item['symbol'] = 'CPNREIT'
            # Nickname Map To Elasticsearch
            self.item['nickName'] = 'เซ็นทรัล CentralPlaza เซ็นทรัลพลาซาลาดพร้าว CentralPlaza Ladprao เซ็นทรัลพลาซารามอินทรา CentralPlaza Ramindra เซ็นทรัลมารีนา CentralPlaza Marina เซ็นทรัลพลาซาปิ่นเกล้า CentralPlaza Pinklao เซ็นทรัลพลาซาเชียงใหม่แอร์พอร์ต CentralPlaza Chiang Mai Airport เซ็นทรัลพลาซาพระราม 3 CentralPlaza Rama 3 เซ็นทรัลพลาซาบางนา CentralPlaza Bangna เซ็นทรัลพลาซาพระราม 2 CentralPlaza Rama 2 เซ็นทรัลพลาซารัตนาธิเบศร์ CentralPlaza Rattanathibet เซ็นทรัลเวิลด์ CentralPlaza World เซ็นทรัลพลาซาแจ้งวัฒนะ CentralPlaza Chaengwattana เซ็นทรัลพลาซาขอนแก่น CentralPlaza KhonKaen เซ็นทรัลพลาซาชลบุรี CentralPlaza Chonburi เซ็นทรัลพลาซาอุดรธานี CentralPlaza UdonThani เซ็นทรัลเฟสติวัลพัทยาบีช CentralPlaza Festival Pattaya Beach เซ็นทรัลพลาซาแกรนด์พระราม 9 CentralPlaza Grand Rama 9 เซ็นทรัลพลาซาพิษณุโลก CentralPlaza Phitsanulok เซ็นทรัลพลาซาเชียงราย CentralPlaza Chiang Rai CentralPlaza เซ็นทรัลพลาซาลำปาง Lampang เซ็นทรัลพลาซาสุราษฎร์ธานี CentralPlaza Suratthani เซ็นทรัลเฟสติวัลหาดใหญ่ CentralPlaza HatYai เซ็นทรัลเฟสติวัลเชียงใหม่ CentralPlaza Chiang Mai เซ็นทรัลพลาซาอุบลราชธานี CentralPlaza Ubon Ratchathani เซ็นทรัลพลาซาศาลายา CentralPlaza Salaya เซ็นทรัลเฟสติวัลสมุย CentralPlaza Samui เซ็นทรัลเฟสติวัลอีสต์วิลล์ CentralPlaza Eastville เซ็นทรัลพลาซาเวสต์เกต CentralPlaza Westgate เซ็นทรัลเฟสติวัลภูเก็ต CentralPlaza Phuket เซ็นทรัลพลาซาระยอง CentralPlaza Rayong เซ็นทรัลพลาซานครศรีธรรมราช CentralPlaza NakhonSiThammarat เซ็นทรัลพลาซามหาชัย CentralPlaza Mahachai เซ็นทรัลพลาซานครราชสีมา CentralPlaza NakhonRatchasima เซ็นลาด เซ็นทรัลลาดพร้าว ลาดพร้าว เซ็นราม เซ็นทรัลรามอินทรา เซ็นมารีนา เซ็นทรัลเซ็นเตอร์พัทยา เซ็นปิ่น เซ็นทรัลปิ่นเกล้า เซ็นแอร์พอร์ต เซ็นทรัลแอร์พอร์ต เซ็นทรัลเชียงใหม่แอร์พอร์ต เซ็นพระราม 3 เซ็นทรัลพระราม 3 เซ็นบางนา เซ็นทรัลบางนา เซ็นพระราม 2 เซ็นทรัลพระราม 2 เซ็นรัตนา เซ็นทรัลรัตนา เซ็นรัตนาธิเบศร์ เซ็นทรัลรัตนาธิเบศร์ เซ็นเวิลด์ เซ็นทรัลเวิลด์ เซ็นแจ้ง เซ็นทรัลแจ้ง เซ็นทรัลเเจ้งวัฒนะ แจ้งวัฒนะ เซ็นทรัลขอนแก่น เซ็นชลบุรี เซ็นทรัลชล เซ็นทรัลชลบุรี เซ็นอุดร เซ็นทรัลอุดรธานี เซ็นบีช เซ็นพัทยาบีช เซ็นทรัลบีช เซ็นทรัลพัทยาบีช เซ็นพระราม 9 เซ็นทรัลพระราม9 เซ็นทรัลแกรนด์พระราม 9 เซ็นพิษณุโลก เซ็นทรัลพิษณุโลก เซ็นทรัลเชียงราย เซ็นทรัลลำปาง เซ็นทรัลสุราษฏร์ เซ็นทรัลสุราษฏร์ธานี เซ็นหาดใหญ๋ เซ็นทรัลเฟสติวัลหาดใหญ่ เซ็นเฟสเชียงใหม่ เซ็นทรัลเฟสติวัลเชียงใหม่ เซ็นอุบล เซ็นทรัลอุบล เซ็นทรัลอุบลราชธานี เซ็นศาลายา เซ็นทรัลศาลายา เซ็นเฟสสมุย เซ็นทรัลเฟสติวัลสมุย เซ็นอีสต์วิลล์ เซ็นทรัลอีสต์วิลล์ เซ็นทรัลเฟสติวัลอีสต์วิลล์ เซ็นเวสต์เกต เซ็นทรัลเวสต์เกต เซ็นบางใหญ่ เซ็นทรัลบางใหญ่ เซ็นเฟสภูเก็ต เซ็นภูเก็ต เซ็นทรัลภูเก็ต เซ็นทรัลเฟสติวัลภูเก็ต เซ็นทรัลระยอง เซ็นทรัลคอน เซ็นทรัลนคร เซ็นทรัลนครศรี เซ็นทรัลนครศรีธรรมราช เซ็นมหาชัย เซ็นทรัลมหาชัย เซ็นนครราชศรีมา เซ็นทรัลนครราชศรีมา '
            # Trustee Map To Elasticsearch
            self.item['trustee'] = 'บริษัท หลักทรัพย์จัดการกองทุน ไทยพาณิชย์ จำกัด'
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
            self.item['establishmentDate'] = '29/11/2017'
            # Registration Date
            self.item['registrationDate'] = '14/12/2560'

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
