import scrapy

from ..items import CarItem

import copy
import time
import random



class ExercarSpider(scrapy.Spider):
    name = 'exercar'
    allowed_domains = ['https://hotels.ctrip.com/']
    start_urls = ['https://hotels.ctrip.com/hotel/Beihai189']

    def parse(self, response):
        urls=response.xpath('//div[@class="list-card-title"]/a/@href').extract()

        for detail_url in urls:
            item = CarItem()
            item['detail_url']=detail_url
            print(detail_url)

            yield scrapy.Request(url=item['detail_url'],callback=self.get_car,
            dont_filter=True,meta={"item":item})

    def get_car(self,response):
        item = response.meta.get('item')
        item['title']=response.xpath('').extract()[0]
        print(item)
        yield item











