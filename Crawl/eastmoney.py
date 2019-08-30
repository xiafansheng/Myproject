import requests
import re
from pyquery import PyQuery as pq

def get_url(date,id,type='hg'):
    url = 'http://data.eastmoney.com/report/{date}/{type},{id}.html'.format(date =date,id = id,type=type)
    return url

def get_pdfurl(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
    res = requests.get(url, headers=headers)
    data = res.text
    doc = pq(data)
    span = doc('.report-content .report-infos a').items()
    for i in span:
        if '查看PDF原文' in str(i):
            url = i.attr('href')
            return url

def download_pdf(url,name):
    path = name+'.pdf'
    r = requests.get(url)
    f = open(r'research report\%s'%path,'wb')
    f.write(r.content)
    f.close()

def get_listinfo(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
    res = requests.get(url,headers=headers)
    data = res.text
    r = re.findall('"(.*?)"',data)
    infolist = [i.split(',') for i in r]
    return infolist

count = 0
baseurl = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=HGYJ&cmd=4&code=&ps=50&p={page}'
for p in range(0,1):
    listurl = baseurl.format(page=p)
#basicurl = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty={HYSR}&stat=0&cmd=4&code=&sc=&ps=50&p={page}'
    infolist = get_listinfo(listurl)
    for x in infolist:
        date = x[0].split(' ')[0].replace('/', '')
        id = x[1]
        num = x[3]
        institute = x[4]
        title = x[-1]
        if '贸易' in title:
            url = get_url(date,id)
            pdfurl = get_pdfurl(url)
            if pdfurl:
                download_pdf(pdfurl,title)
                count+=1
                print('第%d个文件已经下载完成'%count)


import os
os.rename()
