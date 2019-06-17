# import requests
# from bs4 import BeautifulSoup
# res=requests.get('https://news.sina.com.cn/china/')
# res.encoding='utf-8'
# # print(res.text)
# soup=BeautifulSoup(res.text,'html.parser')
# news=soup.select('.news-2')
# # print(news)
# # soup.select()时一个list
# for new in news:
#   if len(new.select('li'))>0:
#            li=new.select('li')
#            a=new.select('a')
#            href=new.select('href')
#            print(href)#输出为[]
#            print(new.text)
##########################
# import requests
# from bs4 import  BeautifulSoup
# res=requests.get('https://news.sina.com.cn/china/')
# res.encoding='utf-8'
# # print(res.text)
# soup=BeautifulSoup(res.text,'html.parser')
# title=soup.select('.page-tools span a')[0].text
# for ti in range(title):
#     print(ti.text)
#soup.select('.news-2')[:-1]#表时去掉了当前所取内容的最后一个P标签
# header=soup.select('a')
# print(header)
# print(header[0])
# for i in range (len(header)+1):
#  print('text........',header[i].text)
# news=soup.select('.main-nav')
# for new in news:
#      if len(new.select('a'))>0:
#          a=new.select('a')
#          href=new.select('href')
#          print(a,href)
#         print(new.text)
#      data=new.select(' data-sudaclick')[0].text
#      time=new.select('a')[0].text
#      a=new.select('a')[0]['i']
#      print(time,data)

# a='<a href="xczxc.com"  abc=34>I am a link</a>'
# soup2=BeautifulSoup(a,'html.parser')
# alink=soup2.select('a')
# for link in alink:
#     print(link['href'])
# import requests
# res=requests.get('https://news.sina.com.cn/c/2019-03-16/doc-ihsxncvh2911998.shtml')
# res.encoding='utf-8'
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(res.text,'html.parser')
# title=soup.select('.main-title')[0].text
# time = soup.select('.date')[0].text
# print(time,title)
# #class  yong .
#id yong #
################################
#requests.patch()  向HTML页面提交局部修改请求的方法，对应于HTTP的PUT
#requests.get() 获取网页头信息的方法，对应与HTTP的get请求
#r=requests.get(url，params=None（url中的额外桉树，字典或字节流格式），**Kwargs(12个控制访问的参数))
# get ：构造一个向服务器请求资源的Request对象
#requests：返回一个包含服务器资源的Response对象  包含爬返回的内容
# import  requests
# r=requests.get("http://www.baidu.com")
# print(r.status_code)
# #若是返回200则可以用r.text  r.enconding r.apparent_enconding  r.content
# #404或其他某些原因出错将产生异常
# r.encoding='utf-8'
# # print(r.text) #拿到了百度主页的内容信息
# print(r.headers)
# print('111111'+r.apparent_encoding)
# print(r.content)  #HTTP响应内容的二进制形式
# print(r.encoding)#http header中猜测的响应内容编码方式
#若header中不存在charset，则认为编码WieISO-8859-1
#r.apparent_encoding从内容中分析出相应内容编码方式（备选编码方式） 根据网页内容分析出编码的方式
###############异常处理  这样让异常处理更加稳定
# import requests
# def getHTMLText(url):
#     try:
#         r=requests.get(url,timeout=30)
#         r.raise_for_status()
#         r.encoding=r.apparent_encoding
#         return r.text
#     except:
#         return "产生异常"
# if __name__=="__main__":
#     url="http://www.baidu.com"
#     print(getHTMLText(url))
#######################
# import urllib
# import urllib3
# requests库的掌握#####################
# requests.request(method,url,**kwargs)
# requests.get()
# requests.head()
# try:
#     return r.text()#如果不是200南无会进入except进行异常处理
# except:
# user agent
# Robots
# http://www.qq.com/robots.txt
# http://news.sina.com.cn/robots.txt
# http://www.baidu.com/robots.txt
# http://moe.edu.cn/robots.txt(无robots协议)
#京东商品信息的爬去

# 获取requestsku
# import  requests
# #获取网络连接
# r=requests.get("https://item.jd.com/2967929.html")
# #返回状态码
# print(r.status_code)#返回的状态码是200   fanhui xinxi zheng que
# #返回编码格式
# print(r.encoding) #返回的编码格式是gbk
# print(r.text[:1000])
#************京东页面内容的盘爬去***************
# import requests
# url="https://item.jd.com/2967929.html"
# try:
#     r=requests.get(url)
#     r.raise_for_status()
#     r.encoding=r.apparent_encoding
#     print(r.text[:1000])
# except:
#     print(r.raise_for_status()+"状态码不是200爬去错误")

#******************亚马逊网页别的爬去********************


# #模拟浏览器访问数据保护较好的网站
# import requests
# url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"
# try:
#     # 现在添加一个可以模仿浏览器的头部键值对逃避拒绝访问
#     kv={'user-agent':'Mozilla/5.0'}
#     r=requests.get(url,headers=kv)
#     r.raise_for_status()
# #////将编码格式转换为可以阅读的编码格式
#     r.encoding=r.apparent_encoding
#     print(r.text[1000:2000])
# except:
#     print(r.raise_for_status()+"爬去失败")
# # print(r.request.headers)   #也就是说我们的头部发送信息被拒绝访问{'User-Agent': 'python-requests/2.18.4', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
#
#************向百度和360搜索引擎中添加关键词提交接口**************
# http://www.baidu.com/s?wd=keyword
# http://www.so.com/s?q=keyword
# import requests
# keyword="python"
# # url="http://baidu.com/s?wd=keyword"  敲黑板
# url="http://baidu.com/s"
# try:
#     kv={'wd':keyword}
#     r=requests.get(url,params=kv)
#     print(r.request.url)
#     r.status_code
#     r.encoding=r.apparent_encoding
#     print(len(r.text))
#     print(r.text[:1000])
# except:
#     print("爬去错误")
#
# import  requests        #二进制度可以 获取
# import os
# url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1558348361860&di=22b8705629854e286b6f49458b967ec9&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201608%2F16%2F20160816183822_hwBM2.jpeg"
# root="/home/happygirl/桌面/wps/pachong/"
# path=root+url.split('/')[-1]
# try:
#     #判断文件夹是否存在
#     if not os.path.exists(root):
#         os.mkdir(root)
#     #判断文件是否存在
#     if not os.path.exists(path):
#         r=requests.get(url)
#         with open(path,'wb')as f:
#             f.write(r.content)
#             f.close()
#             print("文件保存成功")
#     else:
#         print("文件已存在")
# except:
#     print("爬去失败")

#********************查询IP地址的归属地***********************
# import requests
# url = "http://m.ip138.com/ip.asp?ip="
# try:
#    r=requests.get(url+'192.168.1.148')
#    print(r.status_code)
#    print(r.text[-500:])   #这里的[-500:] 指的是只返回后五百的字节
# except:
#     print("爬去失败")
#************** Beautifulsoup ******************

# from bs4 import BeautifulSoup
# import requests
# r=requests.get("http://www.icourse163.org/home.htm?userId=5968045#/home/course")
# demo=r.text
# soup=BeautifulSoup(demo,'html.parser')
# print(soup.prettify())   #prettify 粉饰美化
# soup.title
# tag=soup.a
# import urllib
# import urllib3
# import requests
# from bs4 import BeautifulSoup
# r=requests.get("http://www.icourse163.org/home.htm?userId=5968045#/home/course")
# demo=r.text
# soup=BeautifulSoup(demo,"html.parser")
# # print(soup.a.name)
# # print(soup.a.parent.parent.parent.parent.parent.parent.parent.name)
# tag=soup.a
# print(type(tag.attrs))
#   .string中表示取出来p标签之间文字的部分
# print(soup.p.string)
# 处理html页面中注释的部分上行遍历下行遍历和平行遍历
# 下行遍历：.contents  .children .descendants子孙节点迭代类型包含所有子孙节点，用于循环遍历，钱两者是单次遍历
# print(soup.head.contents)
# print("********************")
# print(soup.body.children)
# print("/////////////////////")
# print(soup.body.descendants)
# print(len(soup.body.contents))
# print(soup.body.contents[1])

# 遍历子孙节点下行遍历
# for child in soup.body.children:
#     print(child)
#     print("********")
#上行遍历对a标签的所有父亲进行打印
#.parent节点的父亲标签
#.parents 节点的先辈标签的迭代类型，用于循环遍历先辈节点
# for parent in soup.a.parents:
#     if parent is None:
#         print("parent:"+parent)
#     else:
#         print(parent.name)
# 平行遍历   其条件是遍历必须发生在用一个父节点下的个节点间
#.next_sibling返回按照HTML文本顺序的下一个平行节点标签
# .previous_sibling 返回按照HTML文本顺序的上一个平行节点标签
#.next_siblings 迭代类型，返回按照HTML文本顺序的后续所有平行节点标签
#.previous_siblings迭代了；类型，返回按照HTML文本顺序的前序所有平行节点标签
# print("1:"+soup.a.next_sibling)
# for sibling in soup.div.next_siblings:
#     print(sibling)
# print("ercibianli ****************************")
# for sibling in soup.previous_siblings:
#     print(sibling)
# //如何让<htlm>代码更加友好的显示
# print(soup.a.prettify())
# 信息提取
# YAML  JSON XML

# from bs4 import BeautifulSoup
# import requests
# import re #正则表达式库
# r=requests.get("https://www.icourse163.org/category/computer")
# demo=r.text
# soup=BeautifulSoup(demo,"html.parser")
# for link in soup.find_all('a'):
#     print(link.get('href'))
# 得到html中的所有连接
# print(soup.find_all('a'))
# for tag in soup.find_all(True):
#     print(tag.name)
# 找到了HTML页面中所有的标签

# **********************************
# <>.find_all(name,attrs,recursive,string,**kwargs)
# 返回的是一个列表类型，存储查找结果
# name:对标签名称的检索字符串

# for tag in soup.find_all(re.compile('b')):
#     print(tag.name)
#
# print("****************************")
# for tag in soup.find_all(re.compile('div')):
#     print(tag.name)
# attrs:对标签属性值的检索字符串，可标注性检索。
# print(demo)
# print(soup.find_all(id=re.compile('sinaads')))
#recursive:是否对子孙全部检索，默认True
# print(soup.find_all('a',recursive=False))
# string:<>...</>中字符串区域的检索字符串
# print(soup.find_all(string=re.compile("计算机")))


#*****************************************************************************************************************************
# http://www.zuihaodaxue.cn.zuihaodaxuepaiming2016.html
#最好大学排名   输入大学paimingURL连接   输出大学排名信息的屏幕输出
#此为定向爬虫：仅对输入URL进行爬去，不扩展爬去
#动态脚本信息的获取使用BS4库是无法爬去的
import urllib3
from bs4 import BeautifulSoup
import requests
import bs4
# r=requests.get("http://www.fortunechina.com/fortune500/c/2018-07/19/content_311046.htm")
# company=r.text
# print(company)
def getHtmlText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return""
def fullTextCompany(comlist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag): #过滤掉非bs4库的tr标签  import bs4
           tds=tr('td')
           comlist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string,tds[4].string,tds[5].string])
def printTextCompany(comlist,num):
    # tplt = "{0:{1}^10}\t{1:{2}^10}\t{2:{3}^10}\t{3:{4}^10}\t{4:{5}^10}\t{5:{6}^10}"  # {1:{3}^10} 1表示位置，{3}表示用第3个参数来填充，^表示居中，10表示占10个位置
    tplt = "{0:^5}\t{1:^5}\t{2:^50}\t{3:^30}\t{4:^20}\t{5:^10}"
    print(tplt.format("排名", "上年排名", "公司名称", "收入","利润","国家",chr(12288)))
    for i in range(num):
        com=comlist[i]
        print(tplt.format(com[0],com[1],com[2],com[3],com[4],com[5],chr(12288)))
def main():
    cominfor=[]
    url="http://www.fortunechina.com/fortune500/c/2018-07/19/content_311046.htm"
    html=getHtmlText(url)
    fullTextCompany(cominfor,html)
    printTextCompany(cominfor,100)
main()
#可见及可爬
#*********************************************************************************************************************************
# 第三周 正则表达式   原生字符串不包含转忆符号









