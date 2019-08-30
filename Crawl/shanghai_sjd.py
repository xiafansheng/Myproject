import requests
from  pyquery import PyQuery as pq
import time
import pandas as pd


headers = {'Accept-Encoding': 'gzip, deflate', 'Cookie': '_gscu_1575893663=51514104u1zq4m54; _gscbrs_1575893663=1; zh_choose=s; ASP.NET_SessionId=xtxfjds0jtkkvcobsi3p2q2h; ASP.NET_SessionId_NS_Sig=oenCV6md0Xpo_Ffi; _gscs_1575893663=517755127h5av721|pv5', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Referer': 'http//service.shanghai.gov.cn/pagemore/iframePagerIndex_4411_3_30.html?page=11', 'Upgrade-Insecure-Requests': '1', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36', 'Connection': 'keep-alive', 'Host': 'service.shanghai.gov.cn'}


def save_to_csv(filename,variblelist):
    df = pd.DataFrame([variblelist])
    #df.columns = headers
    df.to_csv('%s.csv'%filename, mode='a', header=False,encoding='gbk')

for i in range(1,6971):
    print(i)
    url = 'http://www.shanghai.gov.cn/nw2/nw2314/nw2315/nw4411/index%s.html'%i
    detailpage = requests.get(url, headers=headers)
    detailpage.encoding = detailpage.apparent_encoding
    doc = pq(detailpage.text)
    li = doc('.row-fluid ul li').items()
    for l in li:
        url = l('a').attr('href')
        title = l('a').text()
        times = l('.listTime').text()
        res = [i,title,times,url]
        save_to_csv('上海市政府--要闻动态',res)
        time.sleep(0.5)

    # li = doc('.ejfzggxw li').items()
    # for l in li:
    #     url = l('a').attr('href')
    #     title = l('.fzggxwmain').text()
    #     time = l('.ejfzggxwright').text()
    #     res = [title,time,url]
    #     save_to_text('上海市政府--要闻动态',res)

# data = open('上海地方金融管理局--业务信息','r',encoding='utf-8').readlines()
# for i in data:
#     if '交易中心' in i:
#         print(i)