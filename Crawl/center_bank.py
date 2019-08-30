from pyquery import PyQuery as pq
import requests
import re
from selenium import webdriver
import pandas as pd
from Office.save_file import save_to_csv
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
driver = webdriver.Chrome()
driver.get('http://data.cnki.net/area/Yearbook/Single/N2006042302?z=D15')
driver.find_element_by_xpath('//*[@id="div_single_r"]/div[2]/a[28]').click()
driver.find_element_by_xpath('//*[@id="div_ml"]/ul/li[6]/a').click()
#driver.find_element_by_xpath('//*[@id="ResultList_jy"]/table/tbody/tr[2]/td[1]/a').click()
data = pq(driver.page_source)
for i in data('.model_a'):
    if '固定资产投资和建筑业' in i:
        print(i)

#N2006042302000003


# def get_page(url):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
#     res = requests.get(url, headers=headers)
#     res.encoding = res.apparent_encoding
#     data = res.json()
#     #doc = pq(data)
#     return data
#
# def get_epage(url):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
#     res = requests.get(url, headers=headers)
#     res.encoding = res.apparent_encoding
#     data = res.text
#     doc = pq(data)
#     return doc
#
# def get_cpage(url):
#     driver = webdriver.Chrome(chrome_options=options)
#     driver.get(url)
#     data = driver.page_source
#     doc = pq(data)
#     return doc
#
#
#
# def China(country='China'):
#     url = 'http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/11040/index1.html'
#     res = get_cpage(url)
#     result = re.findall('<table cellspacing="0" cellpadding="0" border="0" width="100%">(.*?)</table>', str(res),
#                         re.S)
#     for r in result:
#         try:
#             link = 'http://www.pbc.gov.cn' + re.findall('href="(.*?)"', r, re.S)[0]
#             new = re.findall('title="(.*?)"', r, re.S)[0]
#             time = re.findall('class="hui12">(.*?)</span></td>', r, re.S)[0]
#             li = [link,new,time,country]
#             save_to_csv('cb',li)
#         except:
#             pass
#
# def American(country='American'):
#     url = 'https://www.federalreserve.gov/json/ne-press.json'
#     data = get_page(url)
#     for d in data:
#         try:
#             types = d['pt']
#             time = d['d']
#             link = 'https://www.federalreserve.gov' + d['l']
#             new = d['t']
#             news = {'link': link, 'new': new, 'time': time, 'country': country}
#             li = [link, new, time, country]
#             save_to_csv('cb', li)
#         except:
#                 pass
#
# def European(country='Europen'):
#     url = 'https://www.ecb.europa.eu/press/pr/date/2019/html/index.en.html'
#     res = get_epage(url)
#     result = re.findall('<dt>(.*?)</dt><dd><span class="doc-title"><a href="(.*?)">(.*?)</a></span>',str(res),re.S)
#     for r in result:
#         time = r[0]
#         link = r[1]
#         new = r[2]
#         li = [link, new, time, country]
#         save_to_csv('cb', li)
#
# def main():
#     China()
#     American()
#     European()
#     df = pd.read_csv('cb')
#     print(df)
#
#
# if __name__ == '__main__':
#     main()
#
#
#
