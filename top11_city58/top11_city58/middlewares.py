# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import scrapy
from scrapy import signals
from scrapy import log
import logging

import requests
import random

from .ua import MY_USER_AGENT


class ProxyMiddleware():
    """
   随机更换 proxy
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    def get_random_proxy(self):
        try:
            response = requests.get('http://127.0.0.1:5010/get')
            if response.status_code == 200:
                proxy = response.text
                return proxy
        except:
            self.get_random_proxy()
        
    def process_request(self, spider, request):
        if request.meta.get('retry_times'):
            proxy = self.get_random_proxy()
            if proxy:
                self.logger.debug('正在使用代理', proxy)
                uri = 'https://{proxy}'.format(proxy=proxy)
                request.meta['proxy'] = uri
                

class RandomUserAgentMiddleware(object):

    def __init__(self):
        self.user_agent = MY_USER_AGENT
        self.logger = logging.getLogger(__name__)

    def process_request(self, request, spider):
        if request.meta.get('retry_times'):
            agent = random.choice(self.user_agent)
            self.logger.debug('正在使用UA', agent)
            request.headers['User-Agent'] = agent
            print(agent)
        

        
    
