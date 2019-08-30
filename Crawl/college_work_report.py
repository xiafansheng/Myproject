
import requests
from Office.save_file import save_to_csv
import re,time
from pyquery import PyQuery as pq
import pandas as pd
import urllib


def get_first_url(keyword):
    url = 'http://www.baidu.com.cn/s?wd=' + urllib.parse.quote(keyword) + '&pn=0'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    data = res.text
    doc = pq(data)
    firstres_url = doc('#content_left .f13 a').eq(0).text()
    return firstres_url

def all_result(keyword,page):
    url = 'http://www.baidu.com.cn/s?wd=' + urllib.parse.quote(keyword) + '&pn=%s'%page
    print(url)
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
    # res = requests.get(url, headers=headers)
    # res.encoding = res.apparent_encoding
    # data = res.text
    # doc = pq(data)
    # li = doc('.result.c-container').items()
    # for l in li:
    #     title = l('h3 a').text()
    #     text = l('.f13 a')#.attr('href')
    #     # # print(text)
    #     link = re.findall('.*?href="(.*?)".*?',str(text),re.S)
    #     time = l('.c-abstract')
    #     summaryinfo = l('.c-abstract').text().split('-')
    #     date,summary = summaryinfo[0],summaryinfo[1]
    #     litem = [dte,title,link,summary]
    #     save_to_csv('newbaidu',litem)
    # #return firstres_url
for i in range(0,50):
    print(i)
    pages = i*10
    all_result('交易所 site:www.shanghai.gov.cn',pages)

# df = pd.read_csv('colleges.csv',encoding='gbk',names=['count','name','website'])
# for  k in df['name'].values:
#     #keyword = k + '就业服务中心'
#     website = get_first_url(keyword)
#     print(website)
    # report_keyword = site+filetype+'2018年就业质量报告'
    # pdfurl = get_first_url(report_keyword)
    # print(pdfurl)

