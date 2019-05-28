# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item




class Top97SmzdmItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()
    title = Field()
    price = Field()
    description = Field()
    score = Field()
    data = Field()
    mall = Field()
    detail_url = Field()
