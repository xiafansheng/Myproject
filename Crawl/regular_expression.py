#--utf-8--
import re
# a = 'one1two2three3four4'
# ret = re.findall(r'(\d+)',a)
# print(ret)
import pandas as pd
a =r'C:\Users\Administrator\Desktop\trade war.txt'
txt = open(a).readlines()
txtlist = [t for t in txt if len(t)>2]
for i in txtlist:
    #r = re.findall('(.*?)月(.*?)日(.*?)',i)
    res = (i.split('日'))
    if len(res) == 2:
        li = [res[0]+'日',res[1][1:]]
        df = pd.DataFrame([li])
        df.to_csv('trade war.csv', mode='a', header=False)
    else:
        print('error')
# res = re.findall(r'(\d{1,2})月.*(\d{1,2})日',txt,re.S)
# #res = re.findall(r'(.*?)年',txt,re.S)
# print(res)