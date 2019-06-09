# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import TvshowItem

class TvshowSpider(CrawlSpider):
    name = 'tvshow'
    allowed_domains = ['www.tvmao.com']
    start_urls = ['https://www.tvmao.com/tvshow/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=u'/html/body/div[3]/div/div[2]/ul/li/p[1]/a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        
        tvshow_item = TvshowItem()
        
        tvshow_item['name'] = response.xpath('/html/body/div[2]/div/div/div[1]/strong/text()').extract_first()
        tvshow_item['score'] = response.xpath('/html/body/div[2]/div/div/div[1]/span/text()').extract_first()
        tvshow_item['follows'] = response.xpath('//*[@id="link_num"]/text()').extract_first()
        tvshow_item['title'] = response.xpath('/html/body/div[4]/div/div[1]/h1/text()').extract_first()
        tvshow_item['description'] = response.xpath('/html/body/div[4]/div/div[2]/div/div[1]/div/p/text()').extract_first()
        tvshow_item['channel'] = response.xpath('/html/body/div[4]/div/div[2]/div/div[2]/a/text()').extract_first()
        tvshow_item['date'] = response.xpath('/html/body/div[4]/div/div[2]/div/div[2]/text()').extract_first()
        tvshow_item['guest'] = response.xpath('/html/body/div[4]/div/div[4]/div/div/ul/li/div[2]/a/text()').extract()
        tvshow_item['fixed_guest'] = response.xpath('/html/body/div[4]/div/div[5]/div/div/ul/li/div[2]/a/text()').extract()
        
        yield tvshow_item
        
