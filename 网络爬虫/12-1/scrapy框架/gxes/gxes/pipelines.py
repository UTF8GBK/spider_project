# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 管道文件：用于存储提取出来
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import time

class GxesPipeline:
    def process_item(self, item, spider):
        print(len(item))
        print('detail_url:', item['detail_url'])  # ,'last_time','detail_url','edu','content','welfare'
        # 1.打开csv文件
        with open(r'D:\py资料\py资料\pyton\网络爬虫\12-1\Scrapy框架\gxes\gxes\file/gxhome.xls', 'a', newline='',encoding='utf-8_sig') as filecsv:
            # 2.定义表头
            filename = [
                'detail_url','title','house_name','house_location','house_type','look_at','count_area','total_price','area_price','house_case'
            ]
            # 3.初始化字典对象
            # f：需要保存的表格名字，fieldnames：定义的表头
            writer = csv.DictWriter(filecsv, fieldnames=filename)
            # writer.writeheader()
            with open(r'D:\py资料\py资料\pyton\网络爬虫\12-1\Scrapy框架\gxes\gxes\file/gxhome.xls', 'r', newline="",encoding='utf-8_sig') as f:

                reader = csv.reader(f)
                # 4.写入表头
                if not [row for row in reader]:
                    writer.writeheader()
                    writer.writerow({
                        'detail_url': item['detail_url'],
                        'title': item['title'],
                        'house_name': item['house_name'],
                        'house_location': item['house_location'],
                        'house_type': item['house_type'],
                        'look_at': item['look_at'],
                        'count_area': item['count_area'],
                        'total_price': item['total_price'],
                        'area_price': item['area_price'],
                        'house_case': item['house_case'],

                    })
                else:
                    # for i in range(len()):
                    writer.writerow({
                        'detail_url': item['detail_url'],
                        'title': item['title'],
                        'house_name': item['house_name'],
                        'house_location': item['house_location'],
                        'house_type': item['house_type'],
                        'look_at': item['look_at'],
                        'count_area': item['count_area'],
                        'total_price': item['total_price'],
                        'area_price': item['area_price'],
                        'house_case': item['house_case'],
                    })
                time.sleep(1)

