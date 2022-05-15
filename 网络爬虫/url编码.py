# 在我们眼中：https://www.baidu.com/s？wd=广西机电
# 在电脑眼中 ：https://www.baidu.com/s?wd=%E5%B9%BF%E8%A5%BF%E6%9C%BA%E7%94%B5

# baidu  ：  https://www.baidu.com/s?   关键字  wd
# 360:https://www.baidu.com/s?                  q
# 搜狗：https://www.sogou.com/s?                 query
# 2345: https://www.baidu.com/s?                word


import urllib.parse  #编码解码模块
parm={
    'wd':'广西机电'
}

# 把py字典格式的数据转换成url  编码
data=urllib.parse.urlencode(parm)  #编码
full_url='https://www.baidu.com/s?'+data
print(full_url)
# 把url编码转换成py字典格式的数据
res=urllib.parse.parse_qs(data)  #解码
print(res)