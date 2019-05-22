# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class ReitItem(scrapy.Item):
    # define the fields for your item here like:
	trustNameTh = Field()       
	trustNameEn = Field()  
	symbol = Field()      
	trustee = Field()         
	address = Field()
	reitManager = Field() 
	propertyManager = Field()
	investmentPolicy = Field()            
	establishmentDate = Field()  
	registrationDate = Field()
	peValue = Field()          
	parNAV = Field()
	dvdYield = Field()
	investmentAmount = Field()      
	parValue = Field()          
	ceilingValue = Field()     
	floorValue = Field() 		                       
	priceOfDay = Field()        
	maxPriceOfDay = Field()     
	minPriceOfDay = Field()     
	nickName = Field()          
	url = Field()				 
	policy = Field()  
