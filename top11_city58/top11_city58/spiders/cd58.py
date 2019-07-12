# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import re

from top11_city58.spiders.catelist_cateid import *
from ..items import City58Item


class Cd58Spider(CrawlSpider):
    name = 'cd58'
#    allowed_domains = ['cd.58.com']
    start_urls = ['https://cd.58.com/job.shtml'
                  + '?utm_source=market&spm=u-2d2yxv86y3v43nkddh1'
                  + '.BDPCPZ_BT&PGTID=0d100000-0006-668b-b010-ce4'
                  + '8d404ce79&ClickID=6']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//*[@id="sidebar-right"]/ul/li/a'), callback=None, follow=True),
        Rule(LinkExtractor(restrict_xpaths='/html/body/div[4]/div[4]/div[1]/div[2]/span[1]/a'), callback=None, follow=True),
        Rule(LinkExtractor(restrict_xpaths='//*[@id="list_con"]/li/div[1]/div[1]/a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        """
        爬取可见数据，并传递给 meta
        """
        j_name = response.xpath('//div[@class="leftCon"]//div[@class="pos_base_info"]/span/text()').extract_first()
        j_salary = response.xpath('//div[@class="leftCon"]//div[@class="pos_base_info"]//span[@class="pos_salary"]/text()').extract_first()
        j_description = response.xpath('/html/body/div[3]/div[3]/div[1]/span/text()').extract_first()
        j_welfare = ','.join(response.xpath('/html/body/div[3]/div[3]/div[1]/div[3]/span/text()').extract())
        j_requirement = response.xpath('/html/body/div[3]/div[3]/div[1]/div[4]/span/text()').extract()
        j_location = response.xpath('/html/body/div[3]/div[3]/div[1]/div[5]/span[2]/text()').extract_first()
        j_detail = ''.join(response.xpath('/html/body/div[3]/div[3]/div[2]/div[1]/div[1]/div[1]/text()').extract())
        c_name = response.xpath('/html/body/div[3]/div[4]/div[1]/div/div[1]/div/div[1]/a/text()').extract_first()
        c_introduction = ''.join(response.xpath('/html/body/div[3]/div[3]/div[2]/div[2]/div[2]/div/div/div/p/text()').extract()).replace('\r', '')
        
        infold_url = 'https://statisticszp.58.com/position/totalcount/?infoId={infoId}&userId={userId}&local=102&cateID={cateID}&referUrl=&callback=jQuery110207744574776136623_1562935850521&_=1562935850522'
        nick = re.search('.*com\/(.*?)\/\d.*', response.url).group(1)
        link = response.xpath('/html/body/div[3]/div[4]/div[1]/div/div[1]/div/div[1]/a/@href').extract_first()
        infoId = re.search('.*\/(\d+)x\.shtml\?psid.*', response.url).group(1)
        userId = re.search('.*\/(\d+)\/\?ent.*', link).group(1)
        if nick in cate_dict.keys():
            cateID = cate_dict.get(nick)
            print(cateID)
        