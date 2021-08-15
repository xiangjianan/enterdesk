BOT_NAME = 'enterdesk'

SPIDER_MODULES = ['enterdesk.spiders']
NEWSPIDER_MODULE = 'enterdesk.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

LOG_LEVEL = 'ERROR'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'enterdesk.pipelines.MyPipeline': 301,
}

# ################## 自定义配置 ###################

# 目标图集url地址，可追加
START_URLS = [
    'https://www.enterdesk.com/bizhi/38947.html',
]

# 图片保存位置（绝对路径）
DOWNLOAD_PATH = '/Users/xjn/Downloads/img'
