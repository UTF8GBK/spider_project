# 模拟搜索引擎，等待用户输入需要爬取的页面
# 将结果页面保存到本地，为xxx。html文件

#
# file,文件的名字或者路径
# mode='r'    文件打开方式  r（读）   w(写)  a+(追加)
# wd   (二进制，字节流)图片，视频，音乐
# encoding=None    编码   utf-8   gbk：支持简体中文与繁体中文
# gbk2342 支持简单中文
#




#
# with open('./text.py','w',encoding='utf-8') as f:
#     # f.write('print(''hello!)'
import urllib.request,urllib.parse
# todo 1 获取网页
from requests import request


def get_contebt(url,st):

    #todo 2.构建伪造头
     headers={
         'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
     }
    # todo 3 构建请求参数
     parm={'wd':st}
      # todo  4 将python 字典转换url编码
     data=urllib.parse.urlencode(parm)
    # todo 5 拼接完整的url
     full_url=url+data
     # todo 6 发送请求
     request=  urllib.request.Request(full_url,headers=headers)
    # todo 7 打开响应内容
     resopnse=urllib.request.urlopen(request)
     # todo  8  读取响应内容并编码
     html=resopnse.read().decode('utf-8')
     print(html)
     with open(st+'_页面.html','w',encoding='utf-8') as f:
         f.write(html)
if __name__ =='__main__':
    st=input('请输入爬取内容:')
    url='https://www.baidu.com/s?'  #todo 确定url
    get_contebt(url,st)  #实参











