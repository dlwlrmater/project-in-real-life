import pandas as pd
import math
from multiprocessing import Process
import time

# 基于用户刷卡时间与相同车牌号上的时间、站点信息整合，获得用户上车数据

# df显示完整行
pd.set_option('display.width',None)

# 多进程所需func
def func(dfpart,file,num):
    # 为了防止warning 先copy一下
    dfpart = dfpart.copy()
    # 建立一个新的list 用来存放对应时间的站点信息
    namelist = []
    # 读取每一条数据的 时间&车牌
    for i,j in zip(dfpart['车牌号'],dfpart['New交易时间']):
        o = ''
        # 读取相对车牌的简化表格
        i1 = pd.read_excel(r'H:\工作\!!!香河\excel_公交\路径数据\\'+file+'_简化_无司机2\\'+i+'_简化无司机2.xlsx',index_col=0)
        # 判断刷卡所在时间
        for j1 in i1['Gps时间']:
            if j1<=j:
                o = j1
            else:
                break
        # list中加入时间的站点
        namelist.append(str(i1[i1['Gps时间'] == o]['其他信息'].values).split(' ')[-1].replace('\']',''))
    # df中新增站点列
    dfpart['NewLocation'] = namelist
    # print(dfpart)
    dfpart.to_excel(r'H:\工作\!!!香河\excel_公交\消费交易明细查询-20210419\\'+ file +str(num)+'.xlsx')
    print(num,'done')

def rrr(name):
    # 读取新的简化之后的 时间站点 对应表
    df = pd.read_excel(r'H:\工作\!!!香河\excel_公交\消费交易明细查询\\'+name+'-简化.xlsx',index_col=0)
    # 根据 车牌号&时间 升序排序
    df = df.sort_values(by=['车牌号','New交易时间'],ascending=[True,True])
    # print(df.head())
    # 获得车牌号唯一值
    a = list(set(df['车牌号']))
    a.sort()
    # 获得唯一值数量
    l = len(a)
    # print(l)
    # 由于有12个CPU 向上取整
    avgl = math.ceil(l/12)
    # 根据每个小list的数量 把车牌号唯一值分为12个list
    lst12 = []
    for i in range(0,l,avgl):
        lst12.append(a[i:i+avgl])

    # 根据分组 划分为12个df
    df1 = df[df['车牌号'].isin(lst12[0])]
    df2 = df[df['车牌号'].isin(lst12[1])]
    df3 = df[df['车牌号'].isin(lst12[2])]
    df4 = df[df['车牌号'].isin(lst12[3])]
    df5 = df[df['车牌号'].isin(lst12[4])]
    df6 = df[df['车牌号'].isin(lst12[5])]
    df7 = df[df['车牌号'].isin(lst12[6])]
    df8 = df[df['车牌号'].isin(lst12[7])]
    df9 = df[df['车牌号'].isin(lst12[8])]
    df10 = df[df['车牌号'].isin(lst12[9])]
    df11 = df[df['车牌号'].isin(lst12[10])]
    df12 = df[df['车牌号'].isin(lst12[11])]

    # print(df1.head(50))
    p1 = Process(target=func,args=(df1,'2019-12-18-周三',1))
    p2 = Process(target=func,args=(df2,'2019-12-18-周三',2))
    p3 = Process(target=func,args=(df3,'2019-12-18-周三',3))
    p4 = Process(target=func,args=(df4,'2019-12-18-周三',4))
    p5 = Process(target=func,args=(df5,'2019-12-18-周三',5))
    p6 = Process(target=func,args=(df6,'2019-12-18-周三',6))
    p7 = Process(target=func,args=(df7,'2019-12-18-周三',7))
    p8 = Process(target=func,args=(df8,'2019-12-18-周三',8))
    p9 = Process(target=func,args=(df9,'2019-12-18-周三',9))
    p10 = Process(target=func,args=(df10,'2019-12-18-周三',10))
    p11 = Process(target=func,args=(df11,'2019-12-18-周三',11))
    p12 = Process(target=func,args=(df12,'2019-12-18-周三',12))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p11.start()
    p12.start()




if __name__ == '__main__':
    x = rrr('2019-12-18-周三')
