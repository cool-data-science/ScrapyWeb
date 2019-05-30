# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from scrapy.http import FormRequest

from ..items import Top78LvyouItem

import json
import re

"""
分析了整个网站，大部分数据都是 ajax 异步处理，格式一致

so 只列出了 3 种数据爬取流程，爬取其他数据请诸如此类

数据大量的话 ， 请用 scrapy_redis

"""

class LvyouSpider(Spider):
    name = 'lvyou'
    allowed_domains = ['lvyou.baidu.com', 'm.ctrip.com']
    start_urls = ['https://lvyou.baidu.com/']
        
    def parse(self, response):
                
        tour_url = 'https://m.ctrip.com/restapi/soa2/14984/json/getTourData'
        activity_url = 'https://m.ctrip.com/restapi/soa2/14984/json/getActivityData'
        bargin_url = 'https://m.ctrip.com/restapi/soa2/14984/json/getBarginData'
        
        yield FormRequest(url=tour_url, formdata={"requestJson":"JTdCJTIyaW1hZ2VXaWR0aCUyMjo0NjAsJTIyaW1hZ2VIZWlnaHQlMjI6MzQ2LCUyMnRhYnMlMjI6JTIyMiwzMiw2NCUyMiwlMjJzdGFyQ2l0eSUyMjoxLCUyMnNpZCUyMjo3MTI1NDksJTIyYWxsaWFuY2VpZCUyMjoyNjMxODcsJTIyc2VjcmV0S2V5JTIyOiUyMjA1YzExZWZlNGYwNzQ1MGFiM2M1NTc4N2YwY2E5OTYzJTIyJTdE"}, callback=self.parse_tour, dont_filter=True)
        yield FormRequest(url=activity_url, formdata={"requestJson":"JTdCJTIyaW1hZ2VXaWR0aCUyMjo0NjAsJTIyaW1hZ2VIZWlnaHQlMjI6MzQ2LCUyMmtleVdvcmQlMjI6JTIyJUU1JThDJTk3JUU0JUJBJUFDJTIyLCUyMnNpZCUyMjo3MTI1NDksJTIyYWxsaWFuY2VpZCUyMjoyNjMxODcsJTIyc2VjcmV0S2V5JTIyOiUyMjA1YzExZWZlNGYwNzQ1MGFiM2M1NTc4N2YwY2E5OTYzJTIyJTdE"}, callback=self.parse_activity, dont_filter=True)
        yield FormRequest(url=bargin_url, formdata={"requestJson":"JTdCJTIyc3RhckNpdHklMjI6MSwlMjJzaWQlMjI6NzEyNTQ5LCUyMmFsbGlhbmNlaWQlMjI6MjYzMTg3LCUyMnNlY3JldEtleSUyMjolMjIwNWMxMWVmZTRmMDc0NTBhYjNjNTU3ODdmMGNhOTk2MyUyMiU3RA=="}, callback=self.parse_bargin, dont_filter=True)

     
     
    def parse_tour(self, response):
        result = json.loads(response.text)
        tab_lists = result.get('tabProductList')
        for n in range(0, 2):
            product_lists = tab_lists[n].get('productList')
            
            for i in range(0, 10):
                product_detail = product_lists[i]
    
                item = Top78LvyouItem()
                
                item['url'] = response.url
                item['affList'] = product_detail['affList'][0:10]
                item['featureList'] = product_detail['featureList'][0:10]
                item['imageUrl'] = product_detail['imageUrl']
                item['price'] = product_detail['price']
                item['productID'] = product_detail['productID']
                item['productName'] = product_detail['productName']
                item['typeName'] = product_detail['typeName']
                item['recommendList'] = product_detail['recommendList']
                
                yield item
                
        product_lts = tab_lists[2].get('productList')
        for x in range(0, 3):
            pro_detail = product_lts[x]
            item = Top78LvyouItem()
            
            item['imageUrl'] = pro_detail['imageUrl']
            item['productID'] = pro_detail['productID']
            item['imageUrl'] = pro_detail['imageUrl']
            item['productName'] = pro_detail['productName']
            item['productUrl'] = pro_detail['productUrl']
            item['typeName'] = pro_detail['typeName']
            
            yield item
        
            
            
    def parse_activity(self, response):
        result = json.loads(response.text)
        product_lists = result.get('productList')
        for n in range(0, 9):
            product_detail = product_lists[n]
            item = Top78LvyouItem()
            
            item['url'] = response.url
            item['productID'] = product_detail['productID']
            item['productName'] = product_detail['productName']
            item['price'] = product_detail['price']
            item['imageUrl'] = product_detail['imageUrl']
            item['typeName'] = product_detail['typeName']
            
            yield item
     
     
    
    def parse_bargin(self, response):
        result = json.loads(response.text)
        product_lists = result.get('productList')
        for n in range(0, 9):
            product_detail = product_lists[n]
            item = Top78LvyouItem()
            
            item['url'] = response.url
            item['departCityID'] = product_detail['departCityID']
            item['imageUrl'] = product_detail['imageUrl']
            item['price'] = product_detail['price']
            item['productID'] = product_detail['productID']
            item['productName'] = product_detail['productName']
            item['typeName'] = product_detail['typeName']
            
            yield item
       
        
        
        
        
        