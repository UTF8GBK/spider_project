import scrapy
from ..items import GxItem
import copy


class GxrcSpider(scrapy.Spider):
    name = 'gxrc'  #爬虫的名字
    allowed_domains = ['www.gxrc.com',"s.gxrc.com"]  #允许爬取的域名，如果不给域名那么这个框架不爬取任何数据
    start_urls = ['https://s.gxrc.com/sJob?schType=1&page=1&pageSize=20&orderType=0&listValue=1&keyword=python']  #第一次需要爬取的网站

    def parse(self, response):        #解析函数 注意：解析函数的名字不可以更改
        conten_li = response.xpath('//div[@id="posList"]/div')
        print(conten_li)
        for i in conten_li:
            item =GxItem()
            item['name'] = i.xpath('string(.//h3/a)').extract()[0]  #岗位的名称
            item['entname'] = i.xpath('.//li[@class="w2"]/a/text()').extract()[0]  #公司的名称
            item['price'] = i.xpath('.//li[@class="w3"]/text()').extract()[0]  #薪资待遇
            item['area'] = i.xpath('.//li[@class="w4"]/text()').extract()[0]  #所在地区
            item['last_time'] = i.xpath('.//li[@class="w5"]/text()').extract()[0]  #发布时间
            detail = i.xpath('.//h3/a/@href').extract()[0]      #详情url
            item['detail_url'] = 'https:'+ detail
            # print(item)
            # url   :这个是request对象请求的url
            # callback=None  回调函数 ：下载器执行完之后数据 放在哪个函数里面进行处理
            # meta = None   函数与函数之间的数据传输参数
    #         # dont_filter = False  调度器过滤：是否让这个调度器过滤重复的url
            yield scrapy.Request(url=item['detail_url'],callback=self.get_detail_data,
                           dont_filter=True,meta={"item":copy.deepcopy(item)})


    def get_detail_data(self,response):
        items = response.meta.get('item')
        items['edu'] = response.xpath('string(//p[@class="detail"])') \
            .extract()[0].split("|")[1]
        items['content'] = response.xpath('string(//pre[@id="examineSensitiveWordsContent"])') \
            .extract()[0].replace('\r\n', '')

        welframe = response.xpath('//ul[@class="clearfix"]')
        a = []
        for i in welframe:
            res = i.xpath('./text()').extract()[0].replace('\r\n', '').replace("''", '').replace(' ', '')
            a.append(res)
        items['welfare'] = "|".join(a).replace('||', '')

        # print(items)
        yield items