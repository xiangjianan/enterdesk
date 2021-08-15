import scrapy
from enterdesk.items import EnterdeskItem
from enterdesk.settings import START_URLS


class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.enterdesk.com']

    start_urls = START_URLS

    def parse(self, response, **kwargs):
        item = EnterdeskItem()
        'https://up.enterdesk.com/edpic/b0/da/70/b0da709db31c1154e61e814afcd8aa03.jpg'
        'https://up.enterdesk.com/edpic_source/b0/da/70/b0da709db31c1154e61e814afcd8aa03.jpg'
        img_url_list = response.xpath('//div[@class="swiper-wrapper"]//a/@src').extract()
        for img_url in img_url_list:
            item['img_url'] = img_url.replace('edpic', 'edpic_source')
            yield item
