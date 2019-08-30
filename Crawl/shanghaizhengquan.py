from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.firefox.options import Options
import requests
url = 'http://api.so.eastmoney.com/bussiness/Web/GetSearchList?type=401&pageindex=1&pagesize=10&keyword=%E6%8F%90%E4%BE%9B%E5%A7%94%E6%89%98%E8%B4%B7%E6%AC%BE&'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
res = requests.get(url, headers=headers)
data = res.json()
da = data['Data']
for i in da:
    print(i['NoticeTitle'],i['Url'],i['NoticeDate'])


