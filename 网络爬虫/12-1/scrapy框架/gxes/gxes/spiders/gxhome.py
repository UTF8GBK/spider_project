import scrapy
from ..items import GxesItem

from ..items import GxesItem
import time
import copy
import random

class GxhomeSpider(scrapy.Spider):


    name = 'gxhome'
    allowed_domains = ['nn.lianjia.com'] #域名
    # for i in range(1, 101):
    start_urls = [f'https://nn.lianjia.com/ershoufang/'] #爬取网站
        # print(start_urls)


    def parse(self, response):

        # item = GxesItem()
        urls = response.xpath('//div[@class="info clear"]/div[@class="title"]/a/@href').extract()  #获取每个二手房的详情链接网址，并保存在列表
        for detail_url in urls:
            # print(detail_url)
            item =GxesItem()
            item['detail_url'] = detail_url


            yield scrapy.Request(url=item['detail_url'], callback=self.parse_info,
                                 dont_filter=True, meta={"item": item})

        for i in range(1,100):

            url = f'https://nn.lianjia.com/ershoufang/pg{i}/'

            test_request = scrapy.Request(url,callback = self.parse)
            yield test_request


            # yield scrapy.Request(url =item['detail_url'],callback=self.parse_info)
            # print(urls         # yield item
    #
    def parse_info(self, response):
        item = response.meta.get('item')
        item['title']          = response.xpath('//div[@class="content"]/div[@class]/h1/text()').extract()[0]    # 房源的标题
        item['house_name']     = response.xpath('//div[@class="communityName"]/a[1]/text()').extract()[0]   # 小区的名称
        item['house_location'] = response.xpath('//div[@class="areaName"]/span[2]/a[1]/text()').extract()[0] # 房源所在地区
        item['house_type']     =response.xpath('//div[@class="room"]/div[1]/text()').extract()[0]  # 户型
        item['look_at'] = response.xpath('//div[@class="type"]/div[1]/text()').extract()[0]  # 房源的朝向
        item['count_area']= response.xpath('string(//div[@class="area"]/div[1])').extract()[0]  # 房源总面积
        item['total_price'] = response.xpath('//span[@class="total"]/text()').extract()[0]  # 总价格
        item['area_price'] = response.xpath('string(//div[@class="unitPrice"]/span[1])').extract()[0]  # 每平方的价格
        item['house_case']=response.xpath('//div[@class="type"]/div[2]/text()').extract()[0]   ##装修情况
        # print(item)
        yield item


    # def start_requests(self):\



    #     url = 'https://nn.lianjia.com/ershoufang/'
    #     for parse in range(2, 100):)
    #
    #         print('正在爬取：第 %s 页' % parse)





    # def main(qu, start_pg=1, end_pg=100, download_times=1):
    #     """爬虫程序
    #     qu: 传入要爬取的qu的拼音的列表
    #     start_pg:开始的页码
    #     end_pg:结束的页码
    #     download_times:第几次下载
    #     """
    #     for q in qu:
    #
    #         # 获取当前区的首页url
    #         url = 'https://qd.lianjia.com/ershoufang/' + q + '/'
    #         # 数据储存的列表
    #         data = []
    #         # 文件保存路径
    #         filename = '二手房-' + q + '第' + str(download_times) + '次下载.csv'
    #
    #         print('二手房-' + q + '第' + str(download_times) + '次下载')
    #         mb = master_bar(range(start_pg, end_pg + 1))
    #
    #         for i in mb:
    #
    #             # 获取每页的url
    #             new_url = url + 'pg' + str(i) + '/'
    #
    #             # 获取当前页面包含的30个房屋详情页的url
    #             url_list = get_url(get(new_url))
    #
    #             for l in progress_bar(range(len(url_list)), parent=mb):
    #
    #                 # 反爬随机停止一段时间
    #                 a = random.randint(2, 5)
    #                 if l % a == 0:
    #                     time.sleep(2 * random.random())
    #
    #                 # 获取当前页面的源码
    #                 text = get(url_list[l])
    #                 # 获取当前页面的房屋信息
    #                 data.append(get_data(text))
    #
    #                 # 反爬随机停止一段时间
    #                 time.sleep(3 * random.random())
    #                 mb.child.comment = '正在爬取第' + str(l + 1) + '条数据!!'
    #             mb.main_bar.comment = '正在爬取第' + str(i + 1) + '页数据!!'
    #
    #             # 反爬随机停止一段时间
    #             time.sleep(5 * random.random())
    #
    #             if i % 5 == 0:
    #                 # 每5页保存一次数据
    #                 pd.DataFrame(data).to_csv(filename, encoding='GB18030')
    #                 mb.write('前' + str(i) + '页数据已保存')


        #

        # for sel in urls:
        #     item = GxesItem()
        #     item['house_name']=house_name_list[i].Field()
        #     item['house_location']=house_location_list
        #     item['house_type']=house_type_list
        #     item['look_at']=look_at_list
        #     item['count_area']=count_area_list
        #     item['total_price']=total_price_list
        #     item['area_price']=area_price_list
        #     item['house_case']=house_case_list
        #     i += 1

        #     has_next_page = urls.xpath(
        #         '//div[@class="page-box fr"]/div[1]/@page-data').extract()[0]
        #     to_dict= eval(has_next_page)
        #     current_page = to_dict['curPage']
        #
        #     if current_page !=100:
        #         next_page=current_page +1
        #         url = ''.join([])
        #         print('starting crapy url:', url)
        #         # 随机爬取时间，防止封ip
        #         time.sleep(round(random.uniform(1, 2), 2))
        #         yield scrapy.Request(url, callback=self.parse)
        #
        #
        #     else:
        #         print('scrapy done!')



    # def data(self,response):


        # house_name = respones.xpath('')



        # content_li=response.xpath('//ul/li/div')
        # print(content_li)
        # for i in content_li:
        #     item=GxesItem()
        #     time.sleep(1)
        #     item['detail_url']=i.xpath('./div/a/@href').extract()  ##详情页的ur
        #     #
        #     print(item)


            # item['house_name']    = i.xpath('//div//div//div/a[@class="info"]').extract()[0]   #小区的名称
            # item['house_location']= i.xpath('//div//div//div[@class="areaName"]/span[@class="info"]').extract()[0]   #房源所在地区
            # item['house_type']    = i.xpath('//div//div/div[@class="houseInfo"]/div[@class="room"]/div[@class="mainInfo"]').extract()[0]  #户型
            # item['look_at']       = i.xpath('//div//div//div[@class="type"]/div[@class="mainInfo"]').extract()[0]   #房源的朝向
            # item['count_area']    = i.xpath('//div//div//div[@class="area"]/div[@class="mainInfo"]').extract()[0] #房源总面积
            # item['total_price']   = i.xpath('//div//div[@class="priceInfo"]/div[@class="totalPrice totalPrice2"]').extract()[0] #总价格
            # item['area_price']    = i.xpath('//div//div[@class="price"]/div/div/span[@class="unitPriceValue"]').extract()[0] #每平方的价格
            # item['house_case']    =i.xpath('//div//div[@class="type"]/div[@class="subInfo"]').extract()[0]   ##装修情况






