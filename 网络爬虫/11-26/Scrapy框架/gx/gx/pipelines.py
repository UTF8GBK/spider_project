# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# 管道文件：用于储存提取出来的数据
# from openpyxl import workbook


import csv

class GxPipeline:
    def process_item(self, item, spider):
            print(len(item))
            print('name:',item['entname'] )#,'last_time','detail_url','edu','content','welfare'
            # 1.打开csv文件
            with open(r'D:\py资料\py资料\pyton\网络爬虫\11-26\Scrapy框架\gx\gx\file/gxrc.csv', 'a', newline='', encoding='utf-8_sig') as filecsv:
                # 2.定义表头
                filename = [
                    'name', 'entname','price','area','last_time','detail_url','edu','content','welfare'
                ]
                # 3.初始化字典对象
                # f：需要保存的表格名字，fieldnames：定义的表头
                writer = csv.DictWriter(filecsv, fieldnames=filename)
                # writer.writeheader()
                with open( r'D:\py资料\py资料\pyton\网络爬虫\11-26\Scrapy框架\gx\gx\file/gxrc.csv','r', newline="",encoding='utf-8_sig') as f:
                    reader = csv.reader(f)
                        # 4.写入表头
                    if not [row for row in reader]:
                        writer.writeheader()
                        writer.writerow({
                                'name': item['name'],
                                'entname': item['entname'],
                                'price': item['price'],
                                'area': item['area'],
                                'last_time': item['last_time'],
                                'detail_url': item['detail_url'],
                                'edu': item['edu'],
                                'content': item['content'],
                                'welfare':item['welfare'],


                            })
                    else:
                        # for i in range(len()):
                            writer.writerow({
                                'name': item['name'],
                                'entname': item['entname'],
                                'price': item['price'],
                                'area': item['area'],
                                'last_time': item['last_time'],
                                'detail_url': item['detail_url'],
                                'edu': item['edu'],
                                'content': item['content'],
                                'welfare': item['welfare'],

                            })
                    # else:
                        # for i in range(len(hero_lis)):
                        #     writer.writerow({
                        #         'heroId': hero_lis[i]['heroId'],
                        #         'name': hero_lis[i]['name']
                        #     })


