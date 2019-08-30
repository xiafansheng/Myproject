import requests
from pyquery import  PyQuery as pq
url = 'https://github.com/trending/python?since=weekly'
res = requests.get(url)
res.encoding = res.apparent_encoding
doc = pq(res.text)
li = doc('li').items()
for l in li:
    link = l('a').attr('href')
    title = l('a').text()
    print(link,title)
