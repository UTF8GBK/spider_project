import scrapy
from ..items import LianjiaItem


class LianjiahousSpider(scrapy.Spider):
    name = 'Lianjiahous'
    allowed_domains = ['nn.lianjia.com']
    start_urls = ['https://nn.lianjia.com/ershoufang/']

    def parse(self, response):
        item = LianjiaItem()
        content_li = response.xpath('//ul[@class="sellListContent"]/li')
        # print(content_li)

        x = 0
        for i in content_li:

            try:

                item['detail_url'] = i.xpath('//div[@class="title"]/a/@href').extract()[x]
                x += 1
                print(item)
                yield scrapy.Request(url=content_li)



