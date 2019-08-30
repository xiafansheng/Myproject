import requests
import re
from pyquery import PyQuery as pq
import pandas as pd
from Office.save_file import save_to_csv

baseurl = 'https://www.p2p001.com/netloan/index/id/9/p/{page}.html'

def get_links(page):
    url = baseurl.format(page=i)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
    res = requests.get(url, headers=headers)
    data = res.text
    doc = pq(data)
    index = doc('#newslist li a').items()
    links = []
    for j in index:
        link = 'https://www.p2p001.com'+j.attr('href')
        links.append(link)
    return links


def parse_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
    res = requests.get(url, headers=headers)
    data = res.text
    doc = pq(data)
    li = []
    for i in [1,3,4,5]:
        tableinfo = doc('#newscontent #tupiantiaozheng table tbody tr').eq(i)('td').items()
        for t in tableinfo:
            res = t.text()
            li.append(res)
    return li


# url = 'https://www.p2p001.com/Netloan/shownews/id/22845.html'
# res = parse_page(url)
# print(res)
#
for i in range(0,112):
    try:
        links = get_links(i)
        for l in links:
            res = parse_page(l)
            save_to_csv('wangdai_data',res)
    except:
        print(i)



#def parse_page(url):
    # table = pd.read_html(url)[0]
    # date = table.iloc[1, :].values[0]
    # df = table.iloc[3:, :]
    # df.columns = table.iloc[2, :].values
    # dates = date.strip('统计日期：').strip('）').split('（')
    # df.index = df.ix[:, 0]
    # df = df[['利率指数', '期限指数', '人气指数', '发展指数']]
    # d = {}
    # d['日期'] = dates[0]
    # d['星期'] = dates[1]
    # dicts = df.to_dict()
    # for k, v in dicts.items():
    #     for x, y in v.items():
    #         d[k + ' : ' + x] = [y]
    # dfs = pd.DataFrame(d)
    # save_dfto_csv('wangdai info appendsss', dfs)


