# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# 定义数据模型的配置文件
import scrapy


class GxItem(scrapy.Item):
    # define the fields for your item here like:
    name       = scrapy.Field()  #岗位的名称
    entname    = scrapy.Field()  #公司的名称
    price      = scrapy.Field()  #薪资待遇
    area       = scrapy.Field()  #所在地区
    last_time  = scrapy.Field()  #发布时间
    detail_url = scrapy.Field()  #详情url
    edu        = scrapy.Field()  #学历
    content    = scrapy.Field()  #任职要求
    welfare    = scrapy.Field()  #福利待遇

