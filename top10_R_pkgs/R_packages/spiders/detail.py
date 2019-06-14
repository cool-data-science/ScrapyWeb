# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import PackagesItem

import re
import pandas as pd

# 分布式爬虫
from scrapy_redis.spiders import RedisCrawlSpider


class DetailSpider(RedisCrawlSpider):
    name = 'detail'
    allowed_domains = ['cran.r-project.org']
    #start_urls = ['https://cran.r-project.org/web/packages/available_packages_by_date.html']
    redis_key = 'DetailSpider:start_urls'
    
    rules = (
        Rule(LinkExtractor(restrict_xpaths=u'//table[@border="1"]/tr/td'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        
        # pd.read_html 方法获取 网页第一个表格
        table1 = pd.read_html(response.url)[0]
        item = PackagesItem()
        
# ## # ##---------------------------------------        
        item['Pkg_name'] = re.findall('.*\/packages\/(.*?)\/index\.html', response.url)[0]
        item['detail_url'] = response.url
        item['title'] = response.xpath('//body//h2/text()').extract_first()
        item['description'] = response.xpath('//html/body/p/text()').extract_first().replace('\n', '')
        item['Version'] = response.xpath('//table[1]/tr[1]/td[2]/text()').extract_first()
        
# ## # ##---------------------------------------
        if 'URL:' in list(table1[0].loc[:]): # 判断字段 是否 在表格行索引里
            col_index = table1[table1[0].loc[:] == 'URL:'].index.tolist() # 索引到该值的 行 位置
            item['URL'] = table1[1].loc[col_index[0]] # 获得 该行 第 2 列的 值
        else:
            item['URL'] = 'NA' # param ~NA: 空值
            
# ## # ##---------------------------------------
        if 'Depends:' in list(table1[0].loc[:]):
            col_index = table1[table1[0].loc[:] == 'Depends:'].index.tolist()
            item['Depends'] = table1[1].loc[col_index[0]]
        else:
            item['Depends'] = 'NA'
            
# ## # ##---------------------------------------        
        if 'Imports:' in list(table1[0].loc[:]):
            col_index = table1[table1[0].loc[:] == 'Imports:'].index.tolist()
            item['Imports'] = table1[1].loc[col_index[0]]
        else:
            item['Imports'] = 'NA'
            
# ## # ##---------------------------------------        
        if 'LinkingTo:' in list(table1[0].loc[:]):
            col_index = table1[table1[0].loc[:] == 'LinkingTo:'].index.tolist()
            item['LinkingTo'] = table1[1].loc[col_index[0]]
        else:
            item['LinkingTo'] = 'NA'
            
# ## # ##---------------------------------------        
        if 'Suggests:' in list(table1[0].loc[:]):
            col_index = table1[table1[0].loc[:] == 'Suggests:'].index.tolist()
            item['Suggests'] = table1[1].loc[col_index[0]]
        else:
            item['Suggests'] = 'NA'
            
# ## # ##---------------------------------------        
        if 'Published:' in list(table1[0].loc[:]):
            col_index = table1[table1[0].loc[:] == 'Published:'].index.tolist()
            item['Published'] = table1[1].loc[col_index[0]]
        else:
            item['Published'] = 'NA'
            
# ## # ##---------------------------------------
        if 'Author:' in list(table1[0].loc[:]):
            col_index = table1[table1[0].loc[:] == 'Author:'].index.tolist()
            item['Author'] = table1[1].loc[col_index[0]]
        else:
            item['Author'] = 'NA'
            
# ## # ##---------------------------------------        
        if 'Maintainer:' in list(table1[0].loc[:]):
            col_index = table1[table1[0].loc[:] == 'Maintainer:'].index.tolist()
            item['Maintainer'] = table1[1].loc[col_index[0]]
        else:
            item['Maintainer'] = 'NA'
            
# ## # ##---------------------------------------
        if 'BugReports:' in list(table1[0].loc[:]):
            col_index = table1[table1[0].loc[:] == 'BugReports:'].index.tolist()
            item['BugReports'] = table1[1].loc[col_index[0]]
        else:
            item['BugReports'] = 'NA'
            
# ## # ##---------------------------------------
        if 'NeedsCompilation:' in list(table1[0].loc[:]):
            col_index = table1[table1[0].loc[:] == 'NeedsCompilation:'].index.tolist()
            item['NeedsCompilation'] = table1[1].loc[col_index[0]]
        else:
            item['NeedsCompilation'] = 'NA'
            
# ## # ##---------------------------------------            
        if 'Language:' in list(table1[0].loc[:]):
            col_index = table1[table1[0].loc[:] == 'Language:'].index.tolist()
            item['Language'] = table1[1].loc[col_index[0]]
        else:
            item['Language'] = 'NA'
            
# ## # ##---------------------------------------        
        if 'Materials:' in list(table1[0].loc[:]):
            col_index = table1[table1[0].loc[:] == 'Materials:'].index.tolist()
            item['Materials'] = table1[1].loc[col_index[0]]
        else:
            item['Materials'] = 'NA'
            
# ## # ##---------------------------------------        
        if 'CRAN\xa0checks:' in list(table1[0].loc[:]):
            col_index = table1[table1[0].loc[:] == 'CRAN\xa0checks:'].index.tolist()
            item['CRAN_checks'] = table1[1].loc[col_index[0]]
        else:
            item['CRAN_checks'] = 'NA'
            
# ## # ##---------------------------------------        
        if 'In\xa0views:' in list(table1[0].loc[:]):
            col_index = table1[table1[0].loc[:] == 'In\xa0views:'].index.tolist()
            item['In_views'] = table1[1].loc[col_index[0]]
        else:
            item['In_views'] = 'NA'
            
# ## # ##---------------------------------------    
        if 'Copyright:' in list(table1[0].loc[:]):
            col_index = table1[table1[0].loc[:] == 'Copyright:'].index.tolist()
            item['Copyright'] = table1[1].loc[col_index[0]]
        else:
            item['Copyright'] = 'NA'
            
# ## # ##---------------------------------------        
        if 'Citation:' in list(table1[0].loc[:]):
            col_index = table1[table1[0].loc[:] == 'Citation:'].index.tolist()
            item['Citation'] = table1[1].loc[col_index[0]]
        else:
            item['Citation'] = 'NA'
            
        yield item
        