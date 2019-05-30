# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.h

import requests

from scrapy.conf import settings

class ProxyMiddleware():
    
    def _get_proxies(self):
        """
        @param : PROXY_URL 代理词网页接口
        """
        proxy = requests.get(settings['PROXY_URL'])
        if proxy.status_code == 200:
            return proxy.text
        else:
            self._get_proxies()

            
    def process_request(self, spider, request):
        proxy= self._get_proxies()
        if proxy:
            uri = 'https://{proxy}'.format(proxy=proxy) 
            request.meta['proxy'] = uri
            
