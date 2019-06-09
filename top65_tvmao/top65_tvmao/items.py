# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Item, Field

class DramaItem(Item):
    score = Field()
    follows = Field()
    name = Field()
    total = Field()
    location = Field()
    actor = Field()
    language = Field()
    directors = Field()
    date = Field()
    screenwriter = Field()
    _type = Field()


class TvshowItem(Item):
    name = Field()
    score = Field()
    follows = Field()
    title = Field()
    description = Field()
    channel = Field()
    date = Field()
    guest = Field()
    fixed_guest = Field()
    
    