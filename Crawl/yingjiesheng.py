import requests
from pyquery import PyQuery as pq
import pandas as pd

class Basicrequest():
    def __init__(self,headers,url,begin_date=1):
        self.headers = headers
        self.url = url
        self.begin_date = begin_date#input('请输入需要获取信息的起始日期')

    def getpage(self):
        webpage = requests.get(self.url,headers = self.headers)
        webpage.encoding = webpage.apparent_encoding
        doc = pq(webpage.text)
        return doc

    def save_to_csv(self,data):
        df = pd.DataFrame(data).T
        df.to_csv('Jobinfo.csv', mode='a', header=False,encoding='utf-8')

class Yingjiesheng(Basicrequest):
    def __init__(self,headers,url):
        super().__init__(headers,url)

    def parsepage(self):
        doc = self.getpage()
        general_info = doc('.tr_list').items()
        title, link, date, source = ([], [], [], [])
        for g in general_info:
            title.append(g('a').text())
            link.append('http://www.yingjiesheng.com'+g('a').attr('href'))
            date.append(g('.date center').text())
            source.append(g('.cols2').text())
        data = [title, link, date, source]
        self.save_to_csv(data)
        return title,link,date,source

    def parsedetail(self,link):
        pass

class Pku_bbs(Basicrequest):
    def __init__(self,headers,url):
        super().__init__(headers,url)

    def parsepage(self):
        doc = self.getpage()
        general_info = doc('html body div#page-content div#page-thread.page-thread div#board-body div#list-body.fw div#list-content.fw div.list-item-topic.list-item').items()
        title, link, date, source = ([], [], [], [])
        for g in general_info:
            title.append(g(' div.title-cont.l div.title.l.limit').text())
            link.append('https://bbs.pku.edu.cn/v2/' + g('a').attr('href'))
            date.append(g(' div.author.l .time').text())
            source.append('北大未名')
        data = [title, link , date, source]
        self.save_to_csv(data)
        return title, link, date, source

    def parsedetail(self,link):
        pass

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0'}
for  p in range(3):
    yingjiesheng = Yingjiesheng(headers,'http://www.yingjiesheng.com/beijing-moreptjob-{page}.html'.format(page = p))
    pkubbs = Pku_bbs(headers,'https://bbs.pku.edu.cn/v2/thread.php?bid=896&mode=topic&page={page}&_pjax=%23page-content'.format(page=p))
    yingjiesheng.parsepage()
    pkubbs.parsepage()


