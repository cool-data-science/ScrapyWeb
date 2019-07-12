"""
浏览量，申请人数，简历投稿数
查询参数需要 cateID
格式 json ｛‘catename’: 'cateid'｝
"""

import requests
from requests.exceptions import ConnectTimeout
import json
import re

def get_cateid():
    url = 'https://j1.58cdn.com.cn/job/pc/full/cate/0.1/jobCates.js?v=0'
    headers = {
         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",   
    }
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            print('爬取成功，开始 re 解析')
            return response
    except ConnectTimeout:
        get_cateid()


def parse_category_info(response):
    cateid = re.findall('cateid\:(.*?)\,', response.text)
    catelist = re.findall('catelist\:"(.*?)"\,', response.text)
    result_dict = dict(zip(catelist, cateid))
    print('解析完成， 开始保存至本地')
    return result_dict


def save_to_local(result):
    with open('catelist_cateid.py', 'a', encoding='utf-8') as f:
        f.write(str(result))
        print('成功')
        
    
if __name__ == '__main__':
    response = get_cateid()
    result = parse_category_info(response)
    save_to_local(result)
    
