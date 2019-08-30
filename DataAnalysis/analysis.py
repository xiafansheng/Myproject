import pandas as pd
from Office.save_file import save_dfto_csv

def split(text):
    if '\t' in text:
        li = text.split('\t')
    else:
        li = text
    return li

def clean(arr):
    newlist =[]
    for li in arr:
        k = [l for l in li if l]
        newlist.append(k)
    return newlist


data = open(r'C:\Users\xfs9619\Desktop\成交数据\2019年05月06日周一.txt').readlines()
da = [d.strip('\n') for d in data]
ranges = []
count = 0
for d in da:
    count+=1
    if 0<len(d)<6:
       ranges.append({d:count})

newranges =[]
for i in range(0,len(ranges)-1):
    infodict = {}
    infodict['name'] = ranges[i].keys()
    infodict['start'] = ranges[i].values()
    infodict['end'] = ranges[i+1].values()
    newranges.append(infodict)
newl = []
for i in newranges:
    name = str(list(i['name'])[0])
    start = int(list(i['start'])[0])
    end = int(list(i['end'])[0])
    newl.apend([name, start, end])
df = pd.DataFrame(newl)
#     if end - start <2:
#         print(name,start,end)
#


    #     pass
    # else:
    #     try:
    #         res = [i.split(' ') for i in da[start:end - 1]]
    #         data = clean(res)
    #         df = pd.DataFrame(data)
    #         dfname = name + str(start) + 'to'+str(end)
    #         df.to_csv('%s.csv'%dfname)
    #     except:
    #         print(name,start,end)

# 				 1389 1481
# 				 1481 1560
# 国债		 1577 1613
# 金融债		 1613 1755
# 地方债		 1755 1775
