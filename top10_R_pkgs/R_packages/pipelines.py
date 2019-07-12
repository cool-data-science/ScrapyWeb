# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class RPackagesPipeline(object):
    
    def __init__(self):
        
        with open('R_pkg_details.csv', 'a', encoding='utf-8') as f:
            # 实例化 csv 对象， 文件名为 R_pkg_details.csv
            self.csv_f = csv.writer(f)
    
    def _set_headers(self): 
            # 设置 表头 
        self.headers = ['Pkg_name', 'Published', 'Author','Version', 'Depends', 'Imports',
                       'LinkingTo', 'Suggests', 'Maintainer', 'BugReports', 'License',
                       'URL', 'NeedsCompilation', 'Language', 'Materials', 'CRAN checks',
                       'title', 'description', 'In views', 'Copyright',
                       'Citation', 'detail_url']
        self.csv_f.writerow(self.headers)
        
    def process_item(self, item, spider):
        
        row = [item['Pkg_name'], item['Published'], item['Author'], item['Version'], item['Depends'], item['Imports'],
               item['LinkingTo'], item['Suggests'], item['Maintainer'], item['BugReports'], item['License'],
               item['URL'], item['NeedsCompilation'], item['Language'], item['Materials'], item['CRAN_checks'], 
               item['title'], item['description'], item['In_views'], item['Copyright'], 
               item['Citation'], item['detail_url']]
        
        self.csv_f.writerow(row)
        print('写入成功! ')
        
        
