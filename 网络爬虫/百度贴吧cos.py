import requests
from lxml import etree
import random

# 获取网页源代码
def get_content(url):
    cookie_li={
        'BIDUPSID=0336456D91512E94CE9EFD8A832EE937; PSTM=1634260153; BDRCVFR[ZBMvf06rj6C]=mk3SLVN4HKm; BAIDUID=0336456D91512E949115B2B8CB27AC83:FG=1; H_PS_PSSID=; BA_HECTOR=20040h2h0h2hag0krg1gmhl5p0q; BAIDU_WISE_UID=wapp_1634260166112_787; __yjs_duid=1_8b1eb605f4af921ad1a36bf6d78b01e21634260166234'
        'BIDUPSID=9111F640177C4654E6731B3B4AC29FB7; PSTM=1634260264; BDRCVFR[ZBMvf06rj6C]=mk3SLVN4HKm; BAIDUID=9111F640177C4654F42D120355884D66:FG=1; H_PS_PSSID=; BAIDUID_BFESS=9111F640177C4654E6731B3B4AC29FB7:FG=1; BA_HECTOR=250kag2401aga0agfq1gmhl970q; BDRCVFR[-y_2RKd59Rn]=mk3SLVN4HKm; delPer=0; PSINO=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDU_WISE_UID=wapp_1634260281306_391; __yjs_duid=1_f71f6ee78ab66a92695e5a30f5607d361634260281414; ab_sr=1.0.1_YzNmNzU4NTE3NDg5ZDhmNzE0MjY3NGRjOGNiMDAyOGRiOGM3NjlmOTQ4MWMxNzE3ZWIyMWNkZjAzMmY1NzYzOTQ2YmRhMmJjNDY2ZTQ3MTg4NGE1ZDhkNDBlOWQyN2E0MDhmM2NhMzE1MjBjOWM2ODljYmQyZjhkOTJmMjkxZDhiZDA3MGFmNzYzODY1NzcyYTJjNzUzODMwY2ViYTY1ZQ=='
             }
    cook=random.choice(cookie_li)
    # todo 2 ;请求头
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
        'cookie':cookie_li,
        'Referer': 'https: // tieba.baidu.com / f?ie = utf - 8 & kw = cos'
    }


    # todo   3 :发送请求
    request=requests.get(url,hraders=headers).content.decode('utf-8')


    # todo   4: 文档解析
    html=etree.HTML(request)
    print(html)
    return html


# 获取所有的帖子链接
def get_tiezilink(html):
    tieziUrls = []
    link_li=html.xpath('//div[@class="t_con cleafix"]/div[2]/div/div/a/@href')
    print(link_li)
    # 遍历所有的帖子
    for link in link_li:

#         拼接完整的url
        url='https://tieba.baidu.com'
        full_url=url * link
        print(full_url)
        tieziUrls.append(full_url)
    return  tieziUrls


# 获取所有图片的链接
def get_Images():
     pass

# 保存图片
def sava_Imges():
    pass

if __name__ == '__main__':
    url='https://tieba.baidu.com/f?ie=utf-8&kw=cos'
    html=get_content(url)
    tiezilink=get_tiezilink(html)

