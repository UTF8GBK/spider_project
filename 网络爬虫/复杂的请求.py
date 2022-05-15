import urllib.request


# 1：确定url地址
url='https://www.gxun.edu.cn/'


# 2： 构建请求头（术语请求体）

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

# 3:      发送请求
# url: 需要获取的网址
# headers={}  ：构建伪装头（请求头）
# method=None   :  请求方式   ：1.get请求:向服务器请求数据       2.post ：向服务器提交数据
# data=None  ： 向服务器提交数据需要的参数
request=urllib.request.Request(url,headers=headers)

# 4.打开响应内容
resopnse= urllib.request.urlopen(request)


# 5.读取响应内容并编码
print(resopnse.read().decode('utf-8'))
