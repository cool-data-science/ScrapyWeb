# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class PackagesItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    title = Field()
    Pkg_name = Field()
    description = Field()
    Version = Field()
    Depends = Field()
    Imports = Field()
    LinkingTo = Field()
    Suggests = Field()
    Published = Field()
    Author = Field()
    Maintainer = Field()
    BugReports = Field()
    License = Field()
    URL = Field()
    NeedsCompilation = Field()
    Language = Field()
    Materials = Field()
    CRAN_checks = Field()
    detail_url = Field()
    In_views = Field()
    Copyright = Field()
    Citation = Field()
    