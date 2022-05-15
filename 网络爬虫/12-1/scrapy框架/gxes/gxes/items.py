# Define here the models for your scraped items
#
# See documentation in:
# 定义数据模型的配置文件
# https://docs.scrapy.org/en/latest/topics/items.html
# 定义数据模型的配置文件
import scrapy


class GxesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    detail_url     =scrapy.Field()    #详情页的url
    title          =scrapy.Field()    #房源的标题
    house_name     =scrapy.Field()    #小区的名称
    house_location =scrapy.Field()    #房源所在地区
    house_type     =scrapy.Field()    #房源的户型
    look_at           =scrapy.Field()    #房源的朝向
    count_area     =scrapy.Field()    #房源总面积
    total_price    =scrapy.Field()    #总价格
    area_price     =scrapy.Field()    #每平方的价格
    house_case     =scrapy.Field()    #装修情况


