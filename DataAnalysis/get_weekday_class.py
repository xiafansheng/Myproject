import pandas as pd
import numpy as np

def get_lesson(weekday):
    df = pd.read_excel(r'C:\Users\Administrator\Desktop\3_3--18级学术型硕士.xlsx',sheet_name='金融学4').ix[1:,1:]
    df.index= df.ix[:,0]
    df.columns = df.ix[0,:]
    lesson = df.to_dict()
    lessons = {}
    for k,v in lesson.items():
        if k !='时间':
            le = {i:j for i,j in v.items() if 'nan' not in str(i) and 'nan' not in str(j) and i != '时间'}
            lessons[k] = le
    lesson = lessons[weekday]
    return lesson


print(get_lesson('二'))
