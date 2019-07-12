# -*- coding: utf-8 -*-

# Scrapy settings for top11_city58 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'top11_city58'

SPIDER_MODULES = ['top11_city58.spiders']
NEWSPIDER_MODULE = 'top11_city58.spiders'



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'top11_city58 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'zh-CN,zh;q=0.9',
#   'user-agent': 'Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Raspbian Chromium/72.0.3626.121 Chrome/72.0.3626.121 Safari/537.36',
#   'cookie': 'id58=zznu+Fy3K9j+xUxxJYS32Q==; mcity=cd; city=cd; 58home=cd; 58tj_uuid=a4eaa51e-07ae-4ef2-84f0-6daaf72d541e; als=0; xxzl_deviceid=1aEuykTC2OCVzxhgKYxR2%2Bu83JSD8zpGRl7U7Rmx46MXr%2B6n%2FwHg0mxnL2o4NCL4; wmda_uuid=bf40e65ee31c413e2fdb4669ae79eec1; wmda_new_uuid=1; gr_user_id=c2f56168-6978-447c-955d-fa9345a0029b; bj58_new_uv=1; bj58_id58s="LXNzN2ZRa3VKMm5EOTM1OA=="; wmda_visited_projects=%3B1731916484865%3B1731918550401%3B1409632296065; _ga=GA1.2.836078046.1555554060; __utma=253535702.836078046.1555554060.1555554060.1556110033.2; __utmz=253535702.1556110033.2.2.utmcsr=cd.58.com|utmccn=(referral)|utmcmd=referral|utmcct=/; hots=%5B%7B%22d%22%3A0%2C%22s1%22%3A%22scrapy%22%2C%22s2%22%3A%22%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AE%B6%22%2C%22n%22%3A%22sou%22%7D%5D; Hm_lvt_3bb04d7a4ca3846dcc66a99c3e861511=1555554080,1556110056; Hm_lvt_e15962162366a86a6229038443847be7=1555554081,1556110059; GA_GTID=0d360415-0006-6ea4-ab93-ddad7daa054b; nearCity=%5B%7B%22cityName%22%3A%22%E6%88%90%E9%83%BD%22%2C%22city%22%3A%22cd%22%7D%5D; 58app_hide=1; scancat=13907%2C13915%2C38675%2C-%2C13916; Hm_lvt_5a7a7bfd6e7dfd9438b9023d5a6a4a96=1556351636,1556372582; mcityName=%E6%88%90%E9%83%BD; cookieuid1=mgjwFVzEXO5MJ/t/Bx5mAg==; bProtectShowed=true; spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT; f=n; commontopbar_new_city_info=102%7C%E6%88%90%E9%83%BD%7Ccd; commontopbar_ipcity=cd%7C%E6%88%90%E9%83%BD%7C0; new_uv=24; utm_source=market; init_refer=https%253A%252F%252Fsp0.baidu.com%252F9q9JcDHa2gU2pMbgoY3K%252Fadrc.php%253Ft%253D06KL00c00fD4F9Y0K7k90nW_R0KLRtuT00000A-Pj7C00000uTlJen.THYdrnv__tT0UWdBmy-bIfK15y7brjF-uHNhnj0srAuWm1f0IHdArDc3PWDdwHI7P1IawbRYrjb1fHczwDwDP1nsnRD3n0K95gTqFhdWpyfqn1D4nj04PjRLnBusThqbpyfqnHm0uHdCIZwsT1CEQvGdUgK_Iy49QWR3QhPEUiqGQ1FbnM-3IW63PHPvPjP8pvwkryT0mLFW5HnYnWDk%2526tpl%253Dtpl_11534_18997_15000%2526l%253D1510755689%2526attach%253Dlocation%25253D%252526linkName%25253D%252525E6%252525A0%25252587%252525E5%25252587%25252586%252525E5%252525A4%252525B4%252525E9%25252583%252525A8-%252525E6%252525A0%25252587%252525E9%252525A2%25252598-%252525E4%252525B8%252525BB%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkText%25253D58%252525E5%25252590%2525258C%252525E5%2525259F%2525258E-%252525E6%25252589%252525BE%252525E5%252525B7%252525A5%252525E4%252525BD%2525259C%2525252C%252525E6%25252589%252525BE%252525E6%25252588%252525BF%252525E5%252525AD%25252590%2525252C%252525E4%252525B9%252525B0%252525E5%2525258D%25252596%252525E4%252525BA%2525258C%252525E6%25252589%2525258B%252525E8%252525BD%252525A6%2525252C%252525E5%2525259B%252525BD%252525E6%252525B0%25252591%252525E7%25252594%2525259F%252525E6%252525B4%252525BB%252525E6%2525259C%2525258D%252525E5%2525258A%252525A1%252525E5%252525B9%252525B3%252525E5%2525258F%252525B0%252525EF%252525BC%25252581%252526xp%25253Did%28%25252522m3190094572_canvas%25252522%29%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FH2%2525255B1%2525255D%2525252FA%2525255B1%2525255D%252526linkType%25253D%252526checksum%25253D108%2526ie%253Dutf-8%2526f%253D8%2526tn%253Dbaidu%2526wd%253D58%2525E5%252590%25258C%2525E5%25259F%25258E%2526rqlang%253Dcn%2526inputT%253D4732; new_session=0; wmda_session_id_1731916484865=1556501381101-3b9b67d0-8045-e59f; sessionid=cb957aba-6674-4a66-b9df-1ff4efe28039; Hm_lvt_5bcc464efd3454091cf2095d3515ea05=1556350407,1556372803,1556419951,1556501588; Hm_lvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1556372875,1556372888,1556420767,1556502254; gr_session_id_b4113ecf7096b7d6=a5ebd4a1-c8df-4f18-bd1a-5ea9581db135; gr_session_id_b4113ecf7096b7d6_a5ebd4a1-c8df-4f18-bd1a-5ea9581db135=true; Hm_lpvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1556502261; ppStore_fingerprint=595FAF384D991573D7944300A00B05DD83FA98D4A7E2A706%EF%BC%BF1556502261312; JSESSIONID=64DC7461CCF9895035BAEF089E9837B9; Hm_lpvt_5bcc464efd3454091cf2095d3515ea05=1556502322',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'top11_city58.middlewares.ProxyMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'top11_city58.middlewares.ProxyMiddleware': 543,
    'top11_city58.middlewares.RandomUserAgentMiddleware': 10,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}


# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'top11_city58.pipelines.Top11City58Pipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
