import requests
import re
from bs4 import BeautifulSoup
import time
from pyquery import PyQuery as pq

def gethtml(geturl):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0'}
    resp = requests.get(geturl,headers=headers)
    resp.encoding = resp.apparent_encoding
    return resp.text
    #bsobj = BeautifulSoup(resp.text, 'html.parser')

def getdetail():
    doc = pq(html)
    joblist = doc('.job_list').text()
    jobj_i = doc('.j_i').text()
    return joblist,jobj_i

def yjs(html,id):
    if id =='yjs':
        doc = pq(html)
        baseinfo = doc('.tr_list').items()
        return baseinfo
    elif id =='pkbbs':
        doc = pq(html)
        baseinfo = doc('html body div#page-content div#page-thread.page-thread div#board-body div#list-body.fw div#list-content.fw div.list-item-topic.list-item').items()
        return baseinfo
    elif id =='smqh':
        doc = pq(html)
        baseinfo = doc('.article-list li').items()
        return baseinfo
    elif id=='sxs':
        replace_dict = {
            '\ueda3': '0',
            '\ue7d5': '1',
            '\uef31': '2',
            '\uec7d': '3',
            '\ue73d': '4',
            '\ue6d0': '5',
            '\ueabe': '6',
            '\uf375': '7',
            '\ue4df': '8',
            '\uf6dd': '9',
        }
        for key, value in replace_dict.items():
            html = html.replace(key, value)
        doc = pq(html)
        baseinfo = doc('.position-list li').items()
        return baseinfo

def getid(u):
    if u==0:
        id ='yjs'
        return id
    elif u==1:
        id ='pkbbs'
        return id
    elif u==2:
        id='smqh'
        return id
    elif u==3:
        id='sxs'
        return id


#
# urls = ['http://www.yingjiesheng.com/beijing-moreptjob-{page}.html','https://bbs.pku.edu.cn/v2/thread.php?bid=896&mode=topic&page={page}','https://exp.newsmth.net/board/experience/174d7f17369868eb0b73ded374c753b4/{page}','https://www.shixiseng.com/interns/c-110100?p={page}']
# for u in range(4):
#      for i in range(30):
#          try:
#              url = urls[u].format(page=i)
#              id = getid(u)
#              html = gethtml(url)
#              base = yjs(html,id)
#              base = [x.text() for x in base]
#              data =[b.split('\n') for b in base]
#              for d in data:
#                 content = ';'.join(d)
#                 contents = content +'\n'
#                 #with open(r'C:\Users\凡尘微人\Desktop\jobinfo.txt', 'a+', encoding='utf-8') as f:
#                     #f.write(contents)
#                 with open(r'jobinfo%s.txt'%id, 'a+', encoding='utf-8') as f:
#                     f.write(contents)
#          except:
#              pass
from  Office.maketime import nowtime
date = nowtime()[:3]
indeurl = 'https://bbs.pku.edu.cn/v2/thread.php?bid=896&mode=topic&page=2'
print(date)