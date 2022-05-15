
# 环境安装{
    # todo 1. pip install request
    # todo 2.xpath的安装:  pip install lxml
    # todo 3.xpath的使用 : 爬虫概念 :1.可以看到的数据可以爬   2、批量爬取数据
    # }

import requests
from lxml import etree

    # todo 1: 获取网页源码
def get_content(url):

    # todo 2:构建伪造头  （就是UA伪装）
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    # todo 3：发送请求  .text：获取文本    .content：二进制    .json():获取类似与字典格式的json数据
    html=requests.get(url=url)
    print(html.url)
    # todo  4 : 文档解析 :规范html标签,并转换xpath属性
    html=etree.HTML(html.content.decode('utf-8'))
    # print(html)
    return html

# todo :获取具体内容
def get_data(content):


    # todo ：使用xpath规则提取所有内容
    content_li=content.xpath('//div[@class="t_con cleafix"]/div[2]/div[2]/div/div')
    # print(content_li)
    # todo:遍历内容列表里面的数据
    with open('lunyu.text','a+',encoding='utf-8') as f:
        for i in content_li:
            data=i .xpath('./text()')[0].replace('\n','').replace(' ','')
            print(data)
            f.write(data)
            f.write('\n')






if __name__ == '__main__':
    url='https://tieba.baidu.com/f?ie=utf-8&kw=%E8%AE%BA%E8%AF%AD&fr=search'
    html= get_content(url)
    get_data(html)