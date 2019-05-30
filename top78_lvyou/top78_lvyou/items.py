# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class Top78LvyouItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    departCityID = Field()
    imageUrl = Field()
    price = Field()
    productID = Field()
    productName = Field()
    typeName = Field()
    score = Field()
    visitor_num = Field()
    content = Field()
    url = Field()
    departCityID = Field()
    featureList = Field()
    recommendList = Field()
    affList = Field()
    productUrl = Field()
