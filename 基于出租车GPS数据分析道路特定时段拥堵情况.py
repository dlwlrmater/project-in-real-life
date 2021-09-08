import pandas as pd
import pandas as pd, datetime
import os
import numpy as np
import math
from math import radians,sin,cos,degrees,atan2,asin,sqrt,pi

input_path = r'F:\中规院\浮动车\2021年03月17日'
ss=1
for root, dirs, files in os.walk(input_path):
    for file in files:
        filename = os.path.join(root, file)
        data = pd.read_excel(filename,header = 1,usecols = [0,1,2,3,8,9])
        data['vid'] = file[:-4]
        data
        if ss == 1:
            temp = data
            ss=2
        else:
            temp = pd.concat([temp,data])
wkd = temp.reset_index(drop=True)
#1.提取高峰时段数据
wkd['time'] = pd.to_datetime(wkd['时间'])
s_date = datetime.datetime(2021,3,17,7,20,0)
e_date = datetime.datetime(2021,3,17,8,20,0)
df = wkd[(wkd['time'] > s_date) & (wkd['time'] < e_date)]

#2.字段分割
df2 = pd.concat([df, df['车辆状态'].str.split(',', expand=True)], axis=1,names=[''])
df2.columns =  ['时间', '速度', '方向', '车辆状态', '经度', '纬度', 'vid','time','点火','北纬','东经','营运','定位','预约','空车']
df = df2[(df2['定位'] == '定位') & (df2['点火'] == '点火')]
df = df[['时间', '速度', '方向',  '经度', '纬度', 'vid','营运','空车']]
df.to_csv(r'F:\中规院\浮动车\出表\df.csv',encoding = 'gbk')

#
sp = pd.read_csv(r'F:/中规院/浮动车/出表/spnx.txt',sep=',')
spnx = spnx[[ 'Join_Count', '时间', '速度', '方向', '经度', '纬度', 'vid', '营运', '空车',
 'OBJECTID', 'Layer','Shape_Leng', '距离']]

#3.车辆在路段的车速
#1起终点
spnx = spnx.sort_values(['vid','时间'])
spnx.reset_index(inplace = True, drop = True)
spnx['front'] = spnx['OBJECTID'].shift(1)
spnx['next'] = spnx['OBJECTID'].shift(-1)
spnx['start'] = spnx.apply(lambda x: 1 if x['OBJECTID'] !=x['front'] else 0, axis = 1)
spnx['end'] = spnx.apply(lambda x: 1 if x['OBJECTID'] !=x['next'] else 0, axis = 1)
spnxv = spnx[spnx['end'] + spnx['start'] >0]

#2检查
spnxv['front'] = spnxv['OBJECTID'].shift(1)
spnxv['next'] = spnxv['OBJECTID'].shift(-1)
spnxv['judge'] = spnxv.apply(lambda spnxv:int(spnxv['OBJECTID'] == spnxv['front']) + int(spnxv['OBJECTID'] == spnxv['next']),axis =1)
spnxc = spnxv[spnxv['judge'] ==1]
spnxc.reset_index(inplace = True, drop = True)

#3生成od表
spnxc['judge'] = spnxc.index//2
spnxcs = spnxc[spnxc['start'] == 1]
spnxce = spnxc[spnxc['start'] == 0]
spnxcs = spnxcs[['时间', '速度', '方向', '经度', '纬度', 'vid', '空车', 
                 'OBJECTID','Layer',  'Shape_Leng',  'judge']]
spnxcs.columns = ['t_o', 'v_o', 'dir_o', 'lng_o', 'lat_o', 
                  'vid', 'state_o','OBJECTID','Layer','Shape_Leng',  'judge']
spnxce = spnxce[['时间', '速度', '方向', '经度', '纬度', 'vid', '空车', 
                 'OBJECTID', 'judge']]
spnxce.columns = ['t_d', 'v_d', 'dir_d', 'lng_d', 'lat_d',
                  'vid','state_d',   'OBJECTID',  'judge']
spnxm = pd.merge(spnxcs,spnxce,how = 'left',on = ['vid', 'OBJECTID', 'judge'])
spnxm = spnxm.dropna()

#4.计算速度
#1计算距离（m）
def haversine(lon1,lat1,lon2, lat2):   
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])  
    dlon = lon2 - lon1   
    dlat = lat2 - lat1   
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
    c = 2 * asin(sqrt(a))   
    r = 6371
    return c * r * 1000   
spnxm['distance'] = spnxm.apply(lambda x:haversine(x['lng_o'],x['lat_o'],x['lng_d'],x['lat_d']),axis = 1)
#2计算时间差
spnxm['t_o'] = pd.to_datetime(spnxm['t_o'])
spnxm['t_d'] = pd.to_datetime(spnxm['t_d'])
spnxm['deltime'] = spnxm.apply(lambda x:(x['t_d'] - x['t_o']).total_seconds(), axis =1)
#3
spnxm['speed'] = spnxm['distance']/spnxm['deltime']*3.6

#5.计算方位角
def getDegree(lonA, latA, lonB,latB):   
    radLatA = radians(latA)  
    radLonA = radians(lonA)  
    radLatB = radians(latB)  
    radLonB = radians(lonB)  
    dLon = radLonB - radLonA  
    y = sin(dLon) * cos(radLatB)  
    x = cos(radLatA) * sin(radLatB) - sin(radLatA) * cos(radLatB) * cos(dLon)  
    brng = degrees(atan2(y, x))  
    brng = (brng + 360) % 360  
    return brng  
spnxm['degree'] = spnxm.apply(lambda x:getDegree(x['lng_o'],x['lat_o'],x['lng_d'],x['lat_d']),axis = 1)
spnxf['方向'] = spnxf['degree'].apply(lambda x:'东' if (x <= 135) & (x>45) else '南' if (x>135) & (x<=225) else  '西' if (x>225) & (x<=315) else '北')

#6.分路段方向统计速度
speed = spnxa[['speed','方向','OBJECTID','Layer']].groupby(['OBJECTID','方向','Layer']).median().reset_index()
rt = speed[speed['方向'].isin(['北','西'])]
lb = speed[speed['方向'].isin(['南','东'])]

rt.to_csv(r'F:\中规院\浮动车\出表\rt.csv',encoding = 'gbk')
lb.to_csv(r'F:\中规院\浮动车\出表\lb.csv',encoding = 'gbk')















