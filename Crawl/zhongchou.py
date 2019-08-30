import requests
import re
from pyquery import PyQuery as pq
import pandas as pd
from Office.save_file import save_to_text


baseurl = 'https://www.p2p001.cn/chips/index/but_color/2/id/37/p/{page}.html'

def get_links(i):
    url = baseurl.format(page=i)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
    res = requests.get(url, headers=headers)
    data = res.text
    doc = pq(data)
    index = doc('#newslist li a').items()
    links = []
    for j in index:
        link = 'https://www.p2p001.cn'+j.attr('href')
        links.append(link)
    return links

def parse_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
    res = requests.get(url, headers=headers)
    data = res.text
    doc = pq(data)
    date = doc('#newscontent p').eq(0).text().strip('来源：第一众筹').strip('')
    res = doc('#newscontent p').eq(2).text()
    #data =re.findall('第一众筹（深圳钱诚互联网金融研究院）发布了(.*?)中国众筹.*?全国众筹成交额(.*?)万元，认筹时间(.*?)天，参与人数(.*?)人，成功率(.*?)。',res,re.S)[0]
    data = re.findall('第一众筹（深圳钱诚互联网金融研究院）发布了(.*?)中国众筹指数日报显示，该日全国众筹成交额(.*?)万元，认筹时间(.*?)天,参与人数(.*?)人，成功率(.*?)。', res, re.S)[0]

    li = [date,data[0],data[1],data[2],data[3]]
    return li


for i in range(39,65):
    try:
        links = get_links(i)
        for l in links:
            res = parse_page(l)
            save_to_text('zhongchou data append.txt',res)
    except:
        print(i)

