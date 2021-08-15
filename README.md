# 「回车桌面」高清壁纸爬虫

### 安装依赖
```
pip3 install -r requirements.txt
```

### 修改配置文件
``` python
# ################## 自定义配置 ###################

# 目标图集url地址，可追加
START_URLS = [
    'https://www.enterdesk.com/bizhi/38947.html',
]

# 图片保存位置（绝对路径）
DOWNLOAD_PATH = '/Users/xjn/Downloads/img'
```

### 运行
```
scrapy crawl img
```
