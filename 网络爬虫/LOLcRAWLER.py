import requests


def get_content(url):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Referer':'https://lol.qq.com/data/info-heros.shtml',
    }
    hero_data= requests.get(url,headers=headers).json()
    print('英雄联盟共有{len(hero_data)}多少个英雄')
    print(hero_data)
    return hero_data

# 提取具体数据
def get_data(hero_data):
    item={}
    hero_lis=[]

    for i in hero_data['hero']:
        item = {}
        item['heroId']=i['heroId']  #id
        item['name']  =i['name']    #英雄标题
        item['alias']  =i['alias']   #英雄别名
        item['title']  =i['title']   #英雄名字
        item['selectAudio']  =i['selectAudio']   #选择声音
        item['banAudio']  =i['banAudio']         #禁用声音
        item['goldPrice']  =i['goldPrice']       #黄金的价格
        item['couponPrice'] = i['couponPrice']   #点券价格
        item['keywords'] = i['keywords']         #关键字
        # print(item)
        item['detali_url']=f'https://game.gtimg.cn/images/lol/act/img/js/hero/{i["heroId"]}.js'
        detali_data=get_content(item['detali_url'])
        # 背景故事
        item['shortBio']= detali_data['hero']['shortBio']
        # 所有皮肤的名字
        skins=detali_data['skins']
        a=[]
        for i in skins:
            skins_name=i['name']

            a.append(skins_name)

        b='|'.join(a)
        item[' skins_name']=b
        print(item)
        hero_lis.append(item)
    return hero_lis





# 保存cav 表格
import csv
def save_csv(hero_lis):

     #todo : 1 打开csv文件
    with open('lol.csv','a',newline="",encoding='utf_8_sig') as filecsv:

        # todo 2 定义表头
        filename=[
            'heroId','name','alias','title','selectAudio',
            'banAudio','goldPrice', 'couponPrice','keywords',
            'detail_url','shortBio','skins_name'
        ]
        # todo 3  初始化对象
        #  f : 需要初始化的文件名字, fieldnames :定义表头
        writer=csv.DictWriter(filecsv,fieldnames=filename)
        with open("lol.csv",'r',newline='',encoding='utf_8_sig') as  f:    #打开文件
            reader = csv.reader(f)   #读取数据
            if  not [row for row in reader]:
                   # todo 4 写入表头
                   writer.writeheader()
                   # todo 5 :写入数据
                   for i in range(len(hero_lis)):
                       writer.writerow({
                           'heroId' : hero_lis [i]['heroId'],
                           'name' :hero_lis [i]['name'],
                           'alias' : hero_lis [i]['alias'],
                           'title' : hero_lis [i]['title'],
                           'selectAudio' : hero_lis [i]['selectAudio'],
                           'banAudio' : hero_lis [i]['banAudio'],
                           'goldPrice' : hero_lis [i]['goldPrice'],
                           'couponPrice' : hero_lis [i]['couponPrice'],
                           'keywords' : hero_lis [i]['keywords'],
                           'detail_url':hero_lis [i]['detail_url'],
                           'shortBio': hero_lis [i] ['shortBio'],
                           'skins_name': hero_lis [i] ['skins_name'],
                       })
            else:
                for i in range(len(hero_lis)):
                    writer.writerow({
                        'heroId': hero_lis[i]['heroId'],
                        'name': hero_lis[i]['name'],
                        'alias': hero_lis[i]['alias'],
                        'title': hero_lis[i]['title'],
                        'selectAudio': hero_lis[i]['selectAudio'],
                        'banAudio': hero_lis[i]['banAudio'],
                        'goldPrice': hero_lis[i]['goldPrice'],
                        'couponPrice': hero_lis[i]['couponPrice'],
                        'keywords': hero_lis[i]['keywords'],
                        'detail_url': hero_lis[i]['detail_url'],
                        'shortBio': hero_lis[i]['shortBio'],
                        'skins_name': hero_lis[i]['skins_name'],
                    })
# 保存所有英雄的图片
def save_Image():
        pass

if  __name__ == '__main__':
    url='https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    hero_data=get_content(url)
    get_data(hero_data)
