from selenium import webdriver
import requests
import pandas as pd
from pyquery import PyQuery as pq
from Office.save_file import save_to_csv
import pandas as pd

df = pd.read_excel(r'C:\Users\xfs9619\Desktop\交易所.xlsx')['企业名称'].values

def get_fullcontent(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/62.0'}
    res = requests.get(url, headers = headers)
    res.encoding = res.apparent_encoding
    data = res.text
    doc = pq(data)
    content = doc.text()
    return content

def save_to_text(filename,variblelist):
    with open('%s'%filename, 'a+', encoding='utf-8',) as f:
        variblelist = [str(x) for x in variblelist]
        content = '\n'.join(variblelist) + '\n' +'\n'
        f.write(content)


for d in df[12:]:
    print(d)
    url = 'https://news.baidu.com/'
    driver = webdriver.Chrome(executable_path=r'C:\Users\xfs9619\AppData\Local\Google\Chrome\Application\chromedriver.exe')
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="ww"]').send_keys(d)
    driver.find_element_by_xpath('//*[@id="s_btn_wr"]').click()
    data = driver.page_source
    doc = pq(data)
    li = doc('.result').items()
    for l in li:
        #print(l)
        title = l('h3 a').text()
        link = l('h3 a').attr('href')
        info = l('p').text().split(' ')
        source = info[0]
        date = info[1]
        content = get_fullcontent(link)
        li = [title,link,source,date,content]
        save_to_csv('%s'%d,li)
        save_to_text('%s.txt'%d,li)
