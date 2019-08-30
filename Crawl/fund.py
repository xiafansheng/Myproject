import requests
import json
import pandas as pd
import time
from Office.maketime import nowtime

#
#
# def save_to_csv(filename,variblelist):
#     df = pd.DataFrame([variblelist])
#     #df.columns = headers
#     df.to_csv('%s.csv'%filename, mode='a', header=False,encoding='gbk')
#
#
# for i in range(1,1054):
#     with open('log.txt', 'a+') as f:
#         cont = '正在爬取第%s页'%i + '\n'
#         f.write(cont)
#     link = 'http://gs.amac.org.cn/amac-infodisc/api/pof/fund?rand=0.44824094774659584&page=%s&size=100'%i
#     headers = {'Origin': 'http//gs.amac.org.cn', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Encoding': 'gzip, deflate', 'Host': 'gs.amac.org.cn', 'Content-Length': '2', 'X-Requested-With': 'XMLHttpRequest', 'Connection': 'keep-alive', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36', 'Content-Type': 'application/json', 'Referer': 'http//gs.amac.org.cn/amac-infodisc/res/pof/fund/index.html'}
#     data = {}
#     html = requests.post(link, headers=headers,data=json.dumps(data))
#     result = html.json()['content']
#     col = ['mandatorName', 'establishDate','putOnRecordDate','managerType', 'id', 'fundName', 'fundNo', 'managerName', 'putOnRecordDate', 'workingState', 'isDeputeManage', 'managerUrl', 'lastQuarterUpdate', 'url']
#
#     for r in result:
#         try:
#             li = [r[c] for c in col]
#             save_to_csv('funddata',li)
#             time.sleep(1)
#         except:
#             with open('log.txt','a+') as f:
#                 content = '第%s页出现一行错误'%i + '\n'
#                 f.write(content)
#
# complete = ['完成','爬取']
# save_to_csv('fundaata',complete)

#
col = ['id','mandatorName', 'establishDate', 'putOnRecordDate', 'managerType', 'id', 'fundName', 'fundNo', 'managerName',
        'putOnRecordDate', 'workingState', 'isDeputeManage', 'managerUrl', 'lastQuarterUpdate', 'url']
df = pd.read_csv('funddata.csv',encoding='gbk')
df.columns = col
df['establishDate'] = df['establishDate'].apply(lambda x:nowtime(x/1000) if len(str(x))>10 else x)
df['putOnRecordDate'] = df['putOnRecordDate'].ix[:,1].apply(lambda x:nowtime(x/1000))
df.to_excel('FundDATA for Shiyao.xlsx')


def part_mean(df):
    length = len(df.values)
    part = df.sort_value(by ='shouyilv').ix[:length*0.3,]['shouyilv'].mean()
    return part
res = df.groupby(['date']).apply(part_mean)

