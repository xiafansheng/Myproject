import requests
import time
from bs4 import BeautifulSoup
url = 'https://bj.lianjia.com/ershoufang/'
page=('gp')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer':'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;wd=&amp;eqid=c3435a7d00006bd600000003582bfd1f'
}

def getprize(lj):
    price = lj.find_all('div',attrs={'class':'priceInfo'})
    tp = []
    for a in price:
        totalPrice =a.span.string
        tp.append(totalPrice)
    return tp
def getinfo(lj):
    houseInfo=lj.find_all('div',attrs={'class':'houseInfo'})
    hi=[]
    for b in houseInfo:
        house=b.get_text()
        hi.append(house)
    return hi

def getgz(lj):
    followInfo=lj.find_all('div',attrs={'class':'followInfo'})
    fi=[]
    for c in followInfo:
        follow=c.get_text()
        fi.append(follow)
    return fi

result=[]
for i in range(1,30):
    i = str(i)
    a = (url + page + i + '/')
    r = requests.get(url=a,headers=headers)
    lj = BeautifulSoup(r.text,'html.parser')
    p = getprize(lj)
    info = getinfo(lj)
    gz = getgz(lj)
    data = zip(p,info,gz)
    for d in data:
        ds = list(d)
        result.append(ds)
print(result)