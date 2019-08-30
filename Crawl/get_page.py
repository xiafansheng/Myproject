from pyquery import PyQuery as pq
import requests
def get_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    data = res.text
    doc = pq(data)
    return doc
