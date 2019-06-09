# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from ..items import DramaItem

class DramaSpider(CrawlSpider):
    name = 'drama'
    allowed_domains = ['www.tvmao.com']
    start_urls = ['https://www.tvmao.com/drama']

    rules = (
       Rule(LinkExtractor(restrict_xpaths=u'/html/body/div[3]/div/ul[1]/li/div/a'), callback='parse_item', follow=True),
       Rule(LinkExtractor(restrict_xpaths=u'/html/body/div[3]/div/ul[2]/li/p/a'), callback='parse_item', follow=True),
       Rule(LinkExtractor(restrict_xpaths=u'/html/body/div[3]/div/ul[3]/li/div/a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
     
        item = ItemLoader(DramaItem(), response=response)
        
        item.add_xpath('score', '/html/body/div[2]/div/div/div[1]/span/text()')
        item.add_xpath('follows', '//*[@id="link_num"]/text()')
        item.add_xpath('name', '/html/body/div[4]/div[2]/div[1]/strong/text()')
        item.add_xpath('total', '//div[@class="section-wrap mt30"]//table[@class="obj_meta"]//tr[1]//td[2][@class="wd250"]//text()',
                       MapCompose(lambda i: i.replace(',', '')), Join())
        item.add_xpath('location', '//div[@class="section-wrap mt30"]//table[@class="obj_meta"]//tr[1]//td[4][@class="wd250"]//text()')
        item.add_xpath('actor', '//div[@class="section-wrap mt30"]//table[@class="obj_meta"]//tr[2]//td[2][@class="wd250"]//text()',
                       MapCompose(lambda i: i.replace(',', '')), Join())
        item.add_xpath('language', '//div[@class="section-wrap mt30"]//table[@class="obj_meta"]//tr[2]//td[4][@class="wd250"]//text()')
        item.add_xpath('directors', '//div[@class="section-wrap mt30"]//table[@class="obj_meta"]//tr[3]//td[2][@class="wd250"]//text()',
                       MapCompose(lambda x: x.strip(), lambda i: i.replace(',', '')), Join())
        item.add_xpath('date', '//div[@class="section-wrap mt30"]//table[@class="obj_meta"]//tr[3]//td[4][@class="wd250"]//text()')
        item.add_xpath('screenwriter', '//div[@class="section-wrap mt30"]//table[@class="obj_meta"]//tr[4]//td[2][@class="wd250"]//text()')
        item.add_xpath('_type', '//div[@class="section-wrap mt30"]//table[@class="obj_meta"]//tr[4]//td[4][@class="wd250"]//text()',
                       MapCompose(lambda x: x.strip(), lambda i: i.replace(',', ''), Join()))
        
        yield item.load_item()
        
