import requests
import csv

# 获取网页源码
def get_content(url):
    # 构建伪造头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    hero_data = requests.get(url, headers=headers).json()
    #print(hero_data)
    return hero_data


# 提取具体数据
def get_data(hero_data):
    #print(f"英雄联盟共有{len(hero_data)}个英雄")
    # 定义一个空列表用来存储所有的英雄信息
    hero_lis = []
    for i in hero_data['hero']:
        item = {}
        item['heroId'] = i['heroId']  # 英雄ID
        item['name'] = i['name']  # 英雄标题
        item['title'] = i['title']  # 英雄的名字
        item['selectAudio'] = i['selectAudio']  # 选择声音
        item['banAudio'] = i['banAudio']  # 禁用声音
        item['goldPrice'] = i['goldPrice']  # 金币价格
        item['couponPrice'] = i['couponPrice']  # 点券
        item['keywords'] = i['keywords']  # 关键字

        # 详情的url
        item['detali_url'] = f"https://game.gtimg.cn/images/lol/act/img/js/hero/{i['heroId']}.js"
        hero_data = get_content(item['detali_url'])
        # 获取短介绍
        item['shortBio'] = hero_data['hero']['shortBio']
        #
        skins = hero_data['skins']
        a = []  # 添加空列表存储所有皮肤的名字
        for i in skins:  #遍历所有的皮肤
            skins_name = i['name']
            a.append(skins_name)#添加所有皮肤到空列表a中
        b = "|".join(a)  #
        item['skins_name'] = b

        print(item)
        hero_lis.append(item)
    return hero_lis

# 保存csv格式
def save_csv(hero_lis):
    #1.打开csv文件
    with open('lol.csv','a',newline='',encoding='utf_8_sig') as filecsv:#a 追加
        #2.定义表头
        filename=[
            'heroId','name'
        ]
        #3.初始化字典对象
        #f：需要保存的表格名字，fieldnames：定义的表头
        writer =  csv.DictWriter(filecsv,fieldnames=filename)
        with open('lol.py','r',newline="") as f:
            reader = csv.reader(f)
            if not [row for row in reader]:
                # 4.写入表头
                writer.writeheader()
                for i in range(len(hero_lis)):
                    writer.writerow({
                        'heroId':hero_lis[i]['heroId'],
                        'name':hero_lis[i]['name']
                    })
            else:
                for i in range(len(hero_lis)):
                    writer.writerow({
                        'heroId':hero_lis[i]['heroId'],
                        'name':hero_lis[i]['name']
                    })

# 保存所有英雄的图片
def save_Images():
    pass


if __name__ == '__main__':
    url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    hero_data = get_content(url)
    hero_lis = get_data(hero_data)
