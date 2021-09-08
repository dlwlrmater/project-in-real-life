import pandas as pd
from os import walk

# 再次清洗除去司机操作行，只留下车辆进出站所产生的数据

path = r'H:\工作\!!!香河\excel_公交\路径数据\2019-12-14-周六_简化\\'
for root,dir,files in walk(path,topdown=False):
    filename = files
    print(filename)
    print(len(filename))
    for i in filename:
        if i[0] != '~':
            df = pd.read_excel(path+i)
            df1=df[(df['其他信息'].str[:2]!='司机') & (df['其他信息'].str[-1]!=' ') ]
            df1.to_excel(path+i.split('.')[0]+'无司机2.xlsx')