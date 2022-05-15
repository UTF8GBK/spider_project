import urllib.request

# urllib   --->1. 使用urllib实现搜索引擎
# request任务    基础使用-->文本获取----->图片----> vip视频---->解决反爬 ------>爬虫框架

# 1：确定url地址
url='http://www.baidu.com'


# 2：  发送请求
request= urllib.request.urlopen(url)


# 3:      读取内容，并编码

html=request.read().decode('utf-8')

print(html)