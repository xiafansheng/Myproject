import requests
import re
from pyquery import PyQuery as pq
url = 'http://github'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
res = requests.get(url, headers=headers)
data = res.text