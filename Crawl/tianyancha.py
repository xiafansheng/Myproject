# import requests
# from  pyquery import PyQuery as pq
# import time
# import pandas as pd
# import re
# from Office.save_file import save_to_csv
# from Crawl.get_cookie_header import get_headers
# from Office.get_random_list import get_random
#
#
# def get_ip():
#     targetUrl = "http://proxy.abuyun.com/switch-ip"
#     proxyUser = "H63TS71945HLM5WP"  # 通行证书
#     proxyPass = "CE0005A62A8D7DCA"
#
#     proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
#         "host": proxyHost,
#         "port": proxyPort,
#         "user": proxyUser,
#         "pass": proxyPass,
#     }
#
#     proxies = {
#         "http": proxyMeta,
#         "https": proxyMeta,
#     }
#     resp = requests.get(targetUrl, proxies=proxies)
#     data = resp.text.split(',')
#     return data[0]+':'+data[2]
#
#
#
# def get_company_links(url):
#     poxy = get_ip()
#     print(poxy)
#     proxies = {'http': 'http://' + poxy,
#                'https': 'https://' + poxy}
#     index_page = requests.get(url, headers=headers,proxies=proxies)
#     requests.adapters.DEFAULT_RETRIES = 5
#     doc = pq(index_page.text)
#     li = doc('.search-result-single .content .header a').items()
#     links = []
#     infos = []
#     for l in li:
#         link = l.attr('href')
#         links.append(link)
#     return links
#
# def parse_detail_page(url):
#     poxy = get_ip()
#     print(poxy)
#     proxies = {'http': 'http://' + poxy,
#                'https': 'https://' + poxy}
#     index_page = requests.get(url, headers=headers,proxies=proxies)
#     requests.adapters.DEFAULT_RETRIES = 5
#     doc = pq(index_page.text)
#     name = doc('.content .header .name').text()
#     sitcation = doc('.content .tag-list-content .tag-list').eq(0).text()
#     detail = doc('.detail .summary').text()
#     li = []
#     infos = doc('#_container_baseInfo table.table.-striped-col.-border-top-none tbody tr td').items()
#     for i in infos:
#         li.append(i.text())
#     datas = [name,sitcation,detail] +li
#     return datas
#
# proxyHost = "http-pro.abuyun.com"
# proxyPort = "9010"
# # 代理隧道验证信息
# proxyUser = "H63TS71945HLM5WP"  # 通行证书
# proxyPass = "CE0005A62A8D7DCA"
#
# baseurl = 'https://www.tianyancha.com/search/p{page}?key=%E4%BA%A4%E6%98%93%E6%89%80&base=sh'
# for j in range(1,39):
#     url = baseurl.format(page=j)
#     print(j)
#     headers = get_headers('h.txt')
#     links = get_company_links(url)
#     time.sleep(2)
#     for l in links:
#         res = parse_detail_page(l)
#         time.sleep(2)
#         save_to_csv('数据',res)


# print(links,infos)
# # length = len(links)
# # for i in range(0,len(links)):
# #     link = links[i]
# #     info = infos[i]
# #     datas = parse_detail_page(link)
# #     result = datas.append(info)
# #     print(result)

from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://www.tianyancha.com/'
driver.get(url)

