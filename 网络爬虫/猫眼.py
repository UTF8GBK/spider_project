# encoding:utf-8
from requests.exceptions import RequestException
import requests
import json
import re
from urllib import request
from bs4 import BeautifulSoup


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?href="(.*?)".*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        yield {
            'index': item[0],
            'jump': item[1],
            'image': item[2],
            'title': item[3],
            'actor': item[4].strip()[3:],
            'time': item[5].strip()[5:],
            'score': item[6] + item[7]
        }


def parse_summary_page(url):
    # url = 'https://maoyan.com/films/1203'
    head = {}
    # 使用代理
    head[
        'User - Agent'] = 'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2843.400'
    req = request.Request(url, headers=head)
    response = request.urlopen(req)
    html = response.read()
    # 创建request对象
    soup = BeautifulSoup(html, 'lxml')
    # 找出div中的内容
    soup_text = soup.find('span', class_='dra')
    # 输出其中的文本
    # print(soup_text.text)
    return soup_text


def write_to_file(content):
    with open('newMaoyanTop100.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset * 10)
    html = get_one_page(url)

    for item in parse_one_page(html):
        # print(item['number'])
        # print(item['jump'])
        jump_url = "https://maoyan.com" + str(item['jump'])
        item['summary'] = str(parse_summary_page(jump_url)).replace("<span class=\"dra\">", "").replace("</span>", "")
        print(item)
        write_to_file(item)

    # 写txt
    # for item in parse_one_page(html):
    #     write_to_file(item['title'])

    # 爬取100张图片
    # path = 'E:\\myCode\\py_test\\MaoyanTop100\\images\\'
    # for item in parse_one_page(html):
    #     urllib.request.urlretrieve(item['image'], '{}{}.jpg'.format(path, item['index']))


if __name__ == '__main__':
    for i in range(10):
        main(i)
