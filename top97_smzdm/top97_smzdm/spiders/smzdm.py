# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_redis.spiders import RedisCrawlSpider

from ..items import Top97SmzdmItem

import re


class SmzdmSpider(RedisCrawlSpider):
    name = 'smzdm'
    allowed_domains = ['www.smzdm.com']
    redis_key = 'SmzdmSpider:start_urls'
#    start_urls = ['http://www.smzdm.com/']

    rules = (
        Rule(LinkExtractor(allow=r'\/fenlei.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        
        item = Top97SmzdmItem()
        
        item['detail_url'] = response.xpath('//*[@id="feed-main-list"]/li[9]/div/div[2]/h5/a/@href').extract_first()
        item['title'] = response.xpath('//*[@id="feed-main-list"]/li[9]/div/div[2]/h5/a/text()').extract_first()
        item['price'] = response.xpath('//*[@id="feed-main-list"]/li[9]/div/div[2]/div[1]/a/text()').extract_first()
        item['description'] = response.xpath('//*[@id="feed-main-list"]/li[9]/div/div[2]/div[3]/text()').extract_first()
        item['score'] = response.xpath('//*[@id="feed-main-list"]/li[9]/div/div[2]/div[4]/div[1]/span/a[1]/span[1]/span/text()').extract_first()
        item['data'] = response.xpath('//*[@id="feed-main-list"]/li[9]/div/div[2]/div[4]/div[2]/span/text()').extract_first()
        item['mall'] = response.xpath('//*[@id="feed-main-list"]/li[9]/div/div[2]/div[4]/div[2]/span/a/text()').extract_first()
        item['url'] = response.url
        
        yield item

        
