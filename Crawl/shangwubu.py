import requests
import re
from pyquery import PyQuery as pq
import pandas as pd
from NLP.translate_api import translate_words
from Office.save_file import save_to_csv

# url = 'http://interview.mofcom.gov.cn/mofcom_interview/front/blgg/query'
# headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Encoding': 'gzip, deflate','Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8','Cache-Control': 'max-age=0','Connection': 'keep-alive','Content-Length': '55','Content-Type': 'application/x-www-form-urlencoded','Cookie': 'JSESSIONID=7092A8D08E85E2F6E86FB09104FBF7C2; sto-id-20480=GECJFINDFAAA','Host': 'interview.mofcom.gov.cn','Origin': 'http://interview.mofcom.gov.cn','Referer': 'http://interview.mofcom.gov.cn/mofcom_interview/front/blgg/query','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
# for j in range(0,50):
#     try:
#         data = {'pageNumber': j,'maxPageNum': 131}
#         res = requests.post(url, headers=headers,data=data)
#         data = res.text
#         doc = pq(data)
#         infolist = doc('li').items()
#         for i in infolist:
#             info = i('a')
#             link = info.attr('href')
#             titles = info.text().split(' ')
#             id = titles[0]
#             title = titles[1]
#             time = titles[-1].strip('')
#             if '美国' in title:
#                 content =[link,id ,title,time]
#                 save_to_csv('商务部涉美公告',content)
#     except:
#         pass




def get_emonths():
    months = []
    for  i in range(1,13):
        month = str(i) + '月'
        emonth = translate_words(month).lower()
        months.append(emonth)
    return months

months = get_emonths()[:11]
for m in months:
    url = 'https://ustr.gov/about-us/policy-offices/press-office/press-releases/2018/%s'%m
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
    res = requests.get(url, headers=headers)
    data = res.text
    doc = pq(data)
    infolist = doc('.listing li').items()
    for i in infolist:
        try:
            link = 'https://ustr.gov/' + i('a').attr('href')
            title = i('a').text()
            time = i.text()
            ztitle = translate_words(title)
            if '中国' in ztitle:
                content = [link,ztitle,title,time]
                save_to_csv('ustr涉中公告',content)
            else:
                pass
        except:
            pass
    #
    #     print(link,ztitle,time)

