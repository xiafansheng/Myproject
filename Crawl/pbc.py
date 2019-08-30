import requests
from pyquery import PyQuery as pq
from Crawl.get_cookie_header import get_headers
from Crawl.download_pdf import download_pdf,download
from selenium import webdriver
import time
import os

options = webdriver.ChromeOptions()
options.add_argument('headless')
headers = get_headers('pbc.txt')
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': r'C:\pycharm project\Crawl\pbc'}
options.add_experimental_option('prefs', prefs)


def get_index():
    url = 'http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125957/index.html'
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    data = driver.page_source
    doc = pq(data)
    li = doc('tr').items()
    result = {}
    for l in li:
        link = l('td a').attr('href')
        title = l('td a').text()
        if '报告' in title:
            lin = 'http://www.pbc.gov.cn' + link
            result[lin] = title
    return result


def get_detail(url):
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="zoom"]/p[2]/a').click()
    time.sleep(8)
    driver.quit()
    # data = driver.page_source
    # cookies = driver.get_cookies()
    # cookie = [item["name"] + "=" + item["value"] for item in cookies]
    # cookiestr = ';'.join(item for item in cookie)
    # pdfurl  = re.findall('.*?<p>附件：<a href="(.*?)">(.*?).pdf</a></p>.*?',data,re.S)
    # link = 'http://www.pbc.gov.cn' + str(pdfurl[0][0])
    # headers['Cookie'] =  cookiestr
    # print(headers)
    # download_pdf(link,'2017年第二季度中国货币政策',headers)

res = get_index()
print(len(res))
# for k,v in res.items():
#     try:
#         get_detail(k)
#     except:
#         pass

#get_detail('http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125957/3307990/3360428/index.html')
#
# res = requests.get(url,headers=headers)
# res.encoding= res.apparent_encoding

#         download_pdf(link,'pbc',title,headers)
