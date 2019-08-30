import pandas as pd
import numpy.random as npr
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import LabelBinarizer, MultiLabelBinarizer
df1,df ,hinfos,house= pd.DataFrame,pd.DataFrame,pd.DataFrame,pd.DataFrame

#pipe
df = pd.DataFrame(dict(A=list('XXXXYYYYYY'),B=range(10)))
s = df.groupby('A').B.pipe(lambda g: df.B / g.transform('sum') / g.ngroups)
print(s)



exit()
#数据均一化
feature = np.array([[]])
minmax_scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
scaled_feature = minmax_scaler.fit_transform(feature)
# create scaler
scaler = preprocessing.StandardScaler()
standardized = scaler.fit_transform(feature)

##文本数组转0-1变量
# create one-hot encoder
one_hot = LabelBinarizer()
one_hot.fit_transform(feature)
pd.get_dummies(list())
df = pd.DataFrame()

# 文本数字映射
scale_mapper = { "Low": 1,"Medium": 2, "High": 3}
# replace feature values with scale
df["Score"].replace(scale_mapper)


# 矩阵flatten
matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(matrix.flatten())
# 矩阵的秩
rank = np.linalg.matrix_rank(matrix)

# 多重条件筛选
df[(df['Sex'] == 'female') & (df['Age'] >= 65)]
#行筛选
df1[df1['dco'].str.contains('精装')]#|df['routable_link/_text'].str.contains('280 E 2nd')]
df1[~df1(['dco'].str.contains('精装')|df1['dco'].str.contains('毛坯'))] # the number of rows that do not contain 'bd' or 'Studio'

##多重索引
df.index.get_level_values('ticker')#.nunique()

# 替换
df['Sex'].replace('female', 'Woman')
df.replace(1, "One")
df.applymap(lambda v: v.strip('" ') if isinstance(v,str) else v)
ipos = df.applymap(lambda x: x if not '"' in str(x) else x.replace('"',''))
#cc_cln = df.applymap(lambda x: x.strip('平米') if isinstance(x,str) else pass)#else np.nan) appaply应用全部多列数据

#重命名
df.rename(columns={'PClass': 'Passenger Class'})
hinfos.reset_index(drop=True, inplace=True)
df.index.name = 'ticker'

df[df['Age'].isnull()]
# 删除列
df.drop('Age', axis=1)
df1 = df.drop(['drop', 'reset'], axis=1)

##列数据操作
df.loc[:, 'name'].str.split('(', expand=True)[0].str.strip().to_frame('name')
df['location'], df['rooms'],df['area'],df['loacation'],df['dco'] = zip(*df.ix[:,1].map(lambda x: x.split('/')[:5]))

def uppercase(x):
    return x.upper()
df['Name'].apply(uppercase)[0:2]
def parse_info(row):
    c = str(row).count('/')
    if c==5:
        location ,rooms ,area ,toward ,dco ,elevator= row.split('/')[:6]
    else:
        location ,rooms ,area ,toward ,dco = row.split('/')[:5]
        elevator = np.nan
    return pd.Series({'location': location, 'rooms': rooms, 'area': area,'toward': toward, 'dco': dco, 'elevator': elevator})
cc = df['drop'].apply(parse_info)
import re
def parse_addy(row):
    st = re.search('(\d)室(\d)厅', row)
    #so_flr = re.search('(?:APT|#)\s+(\d+)[A-Z]+,', r)
    if st:
        shi = st.group(1)
        ting = st.group(2)
    else:
        shi = np.nan
        ting = np.nan
    return pd.Series({'shi':shi, 'ting':ting})
st = df['rooms'].apply(parse_addy)

#行数据操作
hinfos.loc[:,'elevator'] = hinfos['elevator'].map(lambda x: '未知' if x==np.NAN else x)
hinfos.loc[:,'area'] = hinfos['area'].astype(float)
mcap = df[df.suffix.str.endswith(('B', 'M'))]
mcap.loc[mcap.suffix == 'symbol', 'marketcap'] *= factor

##分组操作
def minmax(arr):
    return arr.max() -arr.max
df[['']].groupby(df['']).agg(['sum','max','minmax'])
df.groupby('Sex').apply(lambda x: x.count())
df.pct_change(1).stack().pipe(lambda x: x.clip(lower=x.quantile(0.01),upper=x.quantile(1-0.01)))

#透视表
hinfos.pivot_table('price', 'location', 'ting', aggfunc='count')
df.marketcap.describe(percentiles=np.arange(.1, 1, .1).round(1)).apply(lambda x: f'{int(x):,d}')
#apply(lambda x: f'{int(x):,d}')大数字转可视化数字
#合并
houseinfo = house.join(cc).join(df['price'])
##两表的行列index相同
df.columns.intersection(house.index)

#可视化
import matplotlib.pyplot as plt
plt.style.use('ggplot')
df['change'].hist(figsize=(15,7), bins=100, color='grey')
#plt.scatter(features[:, 0], features[:, 1], c=target)


#计算收益率
# outlier_cutoff = 0.01
# data = pd.DataFrame()
# lags = [1, 2, 3, 6, 9, 12]
# for lag in lags:
#     data[f'return_{lag}m'] = monthly_prices.pct_change(lag).stack() .pipe(lambda x: x.clip(lower=x.quantile(outlier_cutoff),upper=x.quantile(1-outlier_cutoff))).add(1).pow(1/lag).sub(1)
# data = data.swaplevel().dropna()
# data.info()
#return_{lag}m'] = monthly_prices.pct_change(lag) .stack().pipe(lambda x: x.clip(lower=x.quantile(outlier_cutoff),upper=x.quantile(1-outlier_cutoff))) .add(1).pow(1/lag).sub(1)