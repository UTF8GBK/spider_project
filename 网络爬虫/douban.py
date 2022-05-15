import requests
from lxml import etree
import random
import time
import re
from pymysql import *
import urllib.request
# 获取网页源码
def get_content(url):
    # 定义cookie池
    cookie_li = [
        'll="118302"; bid=FrodNy2KNc8; _vwo_uuid_v2=DEA2A2C9AEF6A43ECC28E1EC66146ADCD|7b24699a37a6063e32995bd523c26c3c; __gads=ID=41753d91b9968014-22175b0963cc006a:T=1633914532:RT=1633914532:S=ALNI_MY0QZx_hoC9cbQQThm5e8iPcRz_-Q; __yadk_uid=vEjHPGeaF9L1bt7jYzakLHDhaCAUSDob; __utmz=30149280.1633944899.7.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1633944901.5.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ct=y; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1634515725%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.237309749.1633914366.1633944899.1634515726.8; __utmb=30149280.0.10.1634515726; __utmc=30149280; __utma=223695111.485603358.1633914366.1633944901.1634515726.6; __utmb=223695111.0.10.1634515726; __utmc=223695111; ap_v=0,6.0; _pk_id.100001.4cf6=189403d6d68435a4.1633914366.6.1634515739.1633945255.',
        'bid=sn8ggEW6Su0; ap_v=0,6.0; __utma=30149280.1639752353.1634515941.1634515941.1634515941.1; __utmb=30149280.0.10.1634515941; __utmc=30149280; __utmz=30149280.1634515941.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.1075599162.1634515941.1634515941.1634515941.1; __utmb=223695111.0.10.1634515941; __utmc=223695111; __utmz=223695111.1634515941.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _pk_id.100001.4cf6=35ababa61dbbb201.1634515942.1.1634515942.1634515942.; _pk_ses.100001.4cf6=*',
        'bid=qLd-WIUZvXU; _pk_id.100001.4cf6=fe8c7a7dccb94018.1634516002.1.1634516002.1634516002.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.845741412.1634516004.1634516004.1634516004.1; __utmb=30149280.0.10.1634516004; __utmc=30149280; __utmz=30149280.1634516004.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.2038781089.1634516004.1634516004.1634516004.1; __utmb=223695111.0.10.1634516004; __utmc=223695111; __utmz=223695111.1634516004.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
    ]
    cookie = random.choice(cookie_li)   # 随机选择cookie
    # todo ： 2.构建伪造头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
        'cookie': cookie ,
        'Referer': 'https://movie.douban.com/',
        'Host': 'movie.douban.com'
    }
    # todo 3. 发送请求
    request = requests.get(url,headers=headers).content.decode('utf-8')
    # print(request)
    # todo : 4. 文档解析
    html = etree.HTML(request)
    print(html)
    return html

# 提取具体的数据
def get_data(html):
    # todo : 获取所有的内容列表
    content_li = html.xpath('//div[@class="indent"]//table')
    # todo : 遍历具体的内容
    data_li = []   # 把所有的数据全部整合在一起，返回数据
    for i in content_li:
        time.sleep(random.randint(1,3))   # 随机返回休眠时间
        item = {}
        item['title'] = i.xpath('.//div[@class="pl2"]/a/text()')[0].replace('/','').replace('\n','').strip()
        item['score'] = i.xpath('.//div[@class="star clearfix"]/span[2]/text()')[0]
        item['number'] = i.xpath('.//div[@class="star clearfix"]/span[3]/text()')[0]\
            .replace('(','').replace(')','').strip('人评价')
        item['detail_url'] = i.xpath('.//div[@class="pl2"]/a/@href')[0]
        item['image_url']  = i.xpath('.//a[@class="nbg"]/img/@src')[0]

        time.sleep(random.randint(1, 5))  # 随机返回休眠时间
        # 定义cookie池
        cookie_li = [
            'll="118302"; bid=FrodNy2KNc8; _vwo_uuid_v2=DEA2A2C9AEF6A43ECC28E1EC66146ADCD|7b24699a37a6063e32995bd523c26c3c; __gads=ID=41753d91b9968014-22175b0963cc006a:T=1633914532:RT=1633914532:S=ALNI_MY0QZx_hoC9cbQQThm5e8iPcRz_-Q; __yadk_uid=vEjHPGeaF9L1bt7jYzakLHDhaCAUSDob; __utmz=30149280.1633944899.7.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1633944901.5.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ct=y; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1634515725%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.237309749.1633914366.1633944899.1634515726.8; __utmb=30149280.0.10.1634515726; __utmc=30149280; __utma=223695111.485603358.1633914366.1633944901.1634515726.6; __utmb=223695111.0.10.1634515726; __utmc=223695111; ap_v=0,6.0; _pk_id.100001.4cf6=189403d6d68435a4.1633914366.6.1634515739.1633945255.',
            'bid=sn8ggEW6Su0; ap_v=0,6.0; __utma=30149280.1639752353.1634515941.1634515941.1634515941.1; __utmb=30149280.0.10.1634515941; __utmc=30149280; __utmz=30149280.1634515941.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.1075599162.1634515941.1634515941.1634515941.1; __utmb=223695111.0.10.1634515941; __utmc=223695111; __utmz=223695111.1634515941.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _pk_id.100001.4cf6=35ababa61dbbb201.1634515942.1.1634515942.1634515942.; _pk_ses.100001.4cf6=*',
            'bid=qLd-WIUZvXU; _pk_id.100001.4cf6=fe8c7a7dccb94018.1634516002.1.1634516002.1634516002.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.845741412.1634516004.1634516004.1634516004.1; __utmb=30149280.0.10.1634516004; __utmc=30149280; __utmz=30149280.1634516004.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.2038781089.1634516004.1634516004.1634516004.1; __utmb=223695111.0.10.1634516004; __utmc=223695111; __utmz=223695111.1634516004.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
        ]
        cookie = random.choice(cookie_li)  # 随机选择cookie
        # todo ： 2.构建伪造头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
            'cookie': cookie,
            'Referer': 'https://movie.douban.com/',
            'Host': 'movie.douban.com'
        }
        html = requests.get(url=item['detail_url'],headers=headers).content.decode('utf-8')
        """
        . : 匹配任意字符,除了换行符 \n
        * : 匹配0个或者多个正则表达式
        ？ ：匹配0个或者1个前面正则表达式
        () : 分组提取
        """
        item['attrs'] = re.findall(r'<span ><span class=.*>导演</span>: .*<a href=".*" rel="v:directedBy">(.*?)</a></span></span><br/>',html)[0]
        item['startdata'] = re.findall(r'<span class="pl">上映日期:</span> .*property="v:initialReleaseDate" content=".*">(.*?)</span><br/>',html)[0]
        item['info'] = re.findall(r'<meta property="og:description" content="(.*?)" />',html)[0]
        print(item)
        data_li.append(item)
    return data_li

# 保存电影封面
def save_image(data_li):
    print(len(data_li))  # 10

    for i in range(len(data_li)):
        time.sleep(random.randint(1,3))  # 随机休眠 1 -3
        filename = f'./static/images/{i+1}.jpg'
        # urllib.request.urlretrieve(data_li[i]['image_url'],filename=filename)
        img = requests.get(data_li[i]['image_url']).content
        with open(filename,'wb') as f:
            f.write(img)

# 保存数据到电影表
def save_moviesInfo(data_li):
    # 创建connection 对象
    conn = connect(host='localhost',port=3306,database='test1',user='root',password='123456',charset='utf8')
    # 创建cursor 对象
    cs1 = conn.cursor()
    # 创建sql 语句
    sql = """
    insert into movies_moviesinfo(title,score,number,image_path,isDelete) values(%s,%s,%s,%s,%s)
    """
    # 插入数据
    for i in range(len(data_li)):
        count = cs1.execute(sql,(data_li[i]['title'],data_li[i]['score'],data_li[i]['number'],
                                 f'/static/image/{i+1}.jpg',0))
    # 提交数据库插入操作
    conn.commit()
    #关闭游标
    cs1.close()
    # 关闭数据库
    conn.close()

# 保存数据到详情表   ->   完善heroInfo
def save_heroInfo():
    pass

if __name__ == '__main__':
    url = 'https://movie.douban.com/chart'
    html = get_content(url)
    data_li = get_data(html)
    # save_image(data_li)
    save_moviesInfo(data_li)
