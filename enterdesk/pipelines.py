# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import requests
from enterdesk.settings import USER_AGENT, DOWNLOAD_PATH


class MyPipeline(object):

    def __init__(self):
        self.path = DOWNLOAD_PATH
        self.headers = {
            'User-Agent': USER_AGENT,
        }

    def open_spider(self, spider):
        print('爬虫开始...')
        try:
            os.mkdir(path=self.path)
        except FileExistsError:
            pass
        print(f'成功创建文件夹{self.path}/')

    # 重写父类方法：该方法会被执行调用多次
    def process_item(self, item, spider):
        img_url = item['img_url']
        img_name = item['img_url'].split('/')[-1]
        img_path = os.path.join(self.path, img_name)
        if os.path.exists(img_path):
            print(f'文件已存在：{img_name}')
            return item
        print(f'正在下载 {img_url}')
        # 将爬虫程序提交的item进行持久化存储
        try:
            response = requests.get(url=img_url, headers=self.headers, timeout=30)
            if response.status_code == 200:
                with open(img_path, 'wb') as f:
                    f.write(response.content)
        except Exception:
            for i in range(1, 10):
                print(f'请求{img_url}超时，尝试第{i}次重复请求')
                response = requests.get(img_url, headers=self.headers, timeout=30)
                if response.status_code == 200:
                    with open(img_path, 'wb') as f:
                        f.write(response.content)
                        break
        print(f'下载完成：{img_name}')
        return item

    # 重写父类方法：结束爬虫时，执行一次
    def close_spider(self, spider):
        print('爬虫结束!')
