import requests
from pyquery import PyQuery as pq
import pandas as pd
import time,json

def save_to_csv(filename,variblelist):
    df = pd.DataFrame([variblelist])
    df.to_csv('%s.csv'%filename, mode='a', header=False,encoding='utf-8')

def get_pykm(pageindex):
    link = 'http://navi.cnki.net/knavi/Common/Search/Journal'
    s = {"StateID":"","Platfrom":"","QueryTime":"","Account":"knavi","ClientToken":"","Language":"","CNode":{"PCode":"CJFD","SMode":"","OperateT":""},"QNode":{"SelectT":"","Select_Fields":"","S_DBCodes":"","QGroup":[{"Key":"Navi","Logic":1,"Items":[],"ChildItems":[{"Key":"Journal","Logic":1,"Items":[{"Key":1,"Title":"","Logic":1,"Name":"168专题代码","Operate":"","Value":"J?","ExtendType":0,"ExtendValue":"","Value2":""}],"ChildItems":[]}]}],"OrderBy":"OTA|DESC","GroupBy":"","Additon":""}}
    data = {'index': '1', 'pagecount': '21', 'pageindex': pageindex, 'displaymode': '1', 'random': '0.3547803485570893'}
    data['SearchStateJson'] = json.dumps(s)
    headers = {'Connection': 'keep-alive', 'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8', 'Accept': 'text/plain, */*; q=0.01', 'Content-Length': '1009', 'Accept-Encoding': 'gzip, deflate', 'Origin': 'http//navi.cnki.net', 'Referer': 'http//navi.cnki.net/knavi/Journal.html', 'Host': 'navi.cnki.net'}
    html = requests.post(link,data=data,headers=headers)
    doc = pq(html.content)
    lis = doc('.list_tup li a').items()
    mag = {}
    for li in lis:
        pykm = li.attr('href')[-4:]
        name = li.attr('title')
        mag[name] = pykm
    return mag

def get_article(pykm,year,issue,name):
    url = 'http://navi.cnki.net/knavi/JournalDetail/GetArticleList?'
    data = {'year': year,'issue':issue ,'pykm':pykm,'pageIdx': 0,'pcode': 'CJFD'}
    headers = {'Host': 'navi.cnki.net','X-Requested-With': 'XMLHttpRequest','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36','Connection': 'keep-alive', 'Origin': 'http//navi.cnki.net', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8','Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '0'}
    html  = requests.post(url,headers = headers,data=data)
    doc = pq(html.text)
    topic = doc('.tit').items()
    articles = doc('dd').items()
    for a in articles:
        title = a('.name a').text()
        author = a('.author').text()
        li = [title,author,year,issue,name]
        save_to_csv('Finance journal',li)


def main():
    issues = [str(0)+str(i) for i in list(range(1,13)) if len(str(i))==1]+[10,11,12]
    #pykms = pd.read_csv('magazine name and code.csv').ix[:,2].values
    pykms  =['JJXD']
    names = pd.read_csv('magazine name and code.csv.csv').ix[:, 1].values
    for year in range(2018,1960,-1):
        for issue in issues:
            for i in range(0, len(pykms)):
                try:
                    get_article(pykms[i], year, issue, names[i])
                    with open('cnkilog.txt','a+',encoding='utf-8') as f:
                        content = pykms[i]+';'+str(year)+';'+issue+';'+names[i]+ 'success' +'\n'
                        f.write(content)
                    time.sleep(3)
                except:
                    with open('cnkilog.txt', 'a+', encoding='utf-8') as f:
                        content = pykms[i] + ';' + str(year) + ';' + issue + ';' + names[i] + 'fail'+'\n'
                        f.write(content)
                    time.sleep(3)


if __name__ == '__main__':
    main()


# issues = [str(0)+str(i) for i in list(range(1,13)) if len(str(i))==1]+[10,11,12]
# for year in range(2018,1960,-1):
#     for issue in issues:
#         get_article('JJXD',year,issue,'经济学动态')