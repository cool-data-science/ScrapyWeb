# -*- coding: utf-8 -*-

# Scrapy settings for top78_lvyou project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'top78_lvyou'

SPIDER_MODULES = ['top78_lvyou.spiders']
NEWSPIDER_MODULE = 'top78_lvyou.spiders'

#PROXY_URL = 'http://127.0.0.1:5010/get'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'top78_lvyou (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'User-Agent': 'Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Raspbian Chromium/72.0.3626.121 Chrome/72.0.3626.121 Safari/537.36',
   'Cookie': 'BAIDUID=F8B8615E7E77BFE4893A22DDD7301A80:FG=1; BIDUPSID=F8B8615E7E77BFE4893A22DDD7301A80; PSTM=1552720991; bdshare_firstime=1559048546457; BDUSS=jFXb0xtSmJyLTBibkczMnhMbEpuYi1zNzk3OWl5MVZnTUhFV0JGeHVPMDVGQlpkSVFBQUFBJCQAAAAAAAAAAAEAAAC9iZXnxOPKx8Snue3C8G5pY2UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADmH7lw5h-5cM; BDLVYEAR=VISITTIME=1559136067143; BDLVMONTH=VISITTIME=1559136067143; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_46c590aaade82326fc76f3ed3ed69f98=1559049345,1559135883,1559179521,1559196872; BDLVDAY=VISITTIME=1559199885764; Hm_lpvt_46c590aaade82326fc76f3ed3ed69f98=1559199886',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'top78_lvyou.middlewares.Top78LvyouSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'top78_lvyou.middlewares.ProxyMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'top78_lvyou.pipelines.Top78LvyouPipeline': 300,
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
