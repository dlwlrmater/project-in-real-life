import pandas as pd
import os
import time
from multiprocessing import Process

# 计算平均出行次数，结合MYSQL使用得到京牌汽车在香河出行情况
# 车辆被拍间隔如果小于30min，则为一次出行

def pa(numberlst,data,num):
    wastetimes = []
    wastetimenames = []
    ddf = pd.DataFrame()
    # print(len(numberlst))
    # print(numberlst)
    n1 = 0
    n2 = 0
    n3 = 0
    # 需要把numberlst里面的['number']所在的dataframe选出来
    df1 = pd.DataFrame()
    # 新建df1减少循环次数
    for j in numberlst:
        pickdf = data[data['number'] == j]
        df1 = df1.append(pickdf)
    # df1应为所有i构成的dataframe
    # print(df1)

    for i in numberlst:
        if len(df1[df1['number'] == i]) ==1:
            ddf = ddf.append(df1[df1.number == i])
            # print('一个'+data[data.number == i])
            n1 +=1
        else:

            n2 += 1
            # 按照去重之后的车牌list选择其出现的所有时间
            name = df1[df1['number']==i]['cross']
            ttime = df1[df1['number']==i]['time']
            # 把sql里面的Timestamp变成从1970年至今的float
            ttime1 = pd.to_datetime(ttime).reset_index(drop=True)
            # 对车出现次数进行for循环
            ddf = ddf.append(df1[(df1.number == i) & (df1.time == ttime.iloc[0])])
            for j in range(len(ttime)-1):
                # pd.Series to list
                n3 +=1
                ttime = list(ttime)
                name = list(name)
                # 如果相差时间少于 XX s 可以输出
                wastetime = (ttime1[j+1].value - ttime1[j].value)/ 1000000000
                wastetimename = i + ' ' +str(ttime[j+1]) + ' ' + str(name[j+1])
                wastetimes.append(wastetime)
                wastetimenames.append(wastetimename)
                # 1800s 30min
                if wastetime > 1800:
                    # print('花费时间:'+str((ttime[j+1].value - ttime[j].value)/ 1000000000))
                    # print('chepai:'+i)
                    # print('输出时间:'+str(ttime[j+1]))
                    # print('------------------')
                    ddf = ddf.append(df1[(df1.number == i) & (df1.time == ttime[j+1])])
                else:
                    pass


        # print(n)
    zzz = pd.DataFrame({'wastetimes':wastetimes,'wastetimenames':wastetimenames})
    # return zzz,ddf
    # print(zzz.head())
    zzz.to_excel('wastetime_total_'+str(num)+'.xlsx')
    ddf.to_excel('result_total_'+str(num)+'.xlsx')
    # print("n1",n1)
    # print("n2",n2)
    # print("n3",n3)
    # a = '京ACK626'
    # print(data[data['number'] == a])
    # print(ddf)


if __name__ == '__main__':
    data = pd.read_csv(r'交警数据-香河.csv')
    # data.rename(columns={'number':'车牌号码','cross':'路口名称','Vehicle Lane':'车道','direction':'方向','chepaitype':'车牌类型','time':'过车时间','km/h':'车速','lengh':'车长','chepaicolor':'车牌颜色','color':'车身颜色','type':'车辆类型','A':'车辆颜色深浅','B':'车辆品牌','C':'车辆子品牌','D':'车辆年款'})
    data.columns = ['number', 'cross', 'Vehicle Lane', 'direction', 'chepaitype', 'time', 'km/h', 'lengh','chepaicolor', 'color', 'type', 'A', 'B', 'C', 'D']
    # print(data.head())
    data = data[['number', 'cross', 'time', 'chepaicolor']]
    # 选择 Number 里面没有车牌的数据
    data = data[-data['number'].isin(['车牌'])]
    # 根据 number time 排序
    data = data.sort_values(by=['number', 'time'], ascending=True)
    # 对index进行重新排序
    data = data.reset_index(drop=True)

    # 选出所有车牌(去重)
    numberlst = list(data['number'].drop_duplicates())
    # 相对合理等分8组
    c = len(numberlst) / 8
    print(c)
    if c >= len(numberlst) // 8 + 0.5:
        c = len(numberlst) // 8 + 1
    else:
        c = len(numberlst) // 8
    b = []
    for i in range(0,len(numberlst),c):
        if i == c*7:
            b.append(numberlst[i:])
            break
        else:
            b.append(numberlst[i:i+c])
    # print(b)
    # 开始计时
    start = time.time()


    p1 = Process(target=pa, args=(b[0], data, '0',))
    p2 = Process(target=pa, args=(b[1], data, '1',))
    p3 = Process(target=pa, args=(b[2], data, '2',))
    p4 = Process(target=pa, args=(b[3], data, '3',))
    p5 = Process(target=pa, args=(b[4], data, '4',))
    p6 = Process(target=pa, args=(b[5], data, '5',))
    p7 = Process(target=pa, args=(b[6], data, '6',))
    p8 = Process(target=pa, args=(b[7], data, '7',))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()

    # 结束计时
    end = time.time()
    result_total = pd.DataFrame()
    wastetime_total = pd.DataFrame()
    for i in range(8):
        df1 = pd.read_excel('result_total_'+str(i)+'.xlsx',index_col=0)
        df2 = pd.read_excel('wastetime_total_'+str(i)+'.xlsx',index_col=0)
        result_total = result_total.append(df1)
        wastetime_total = wastetime_total.append(df2)
    result_total = result_total.reset_index(drop=True)
    wastetime_total = wastetime_total.reset_index(drop=True)
    # del result_total['Unnamed: 0']
    # del wastetime_total['Unnamed: 0']
    result_total.to_excel('result_total.xlsx')
    wastetime_total.to_excel('wastetime_total.xlsx')
    for root,dirs,files in os.walk('.'):
        for i in files:
            if i.split('.')[1] == 'xlsx':
                if len(i.split('.')[0].split('_')) > 1:
                    if i.split('.')[0].split('_')[-2] == 'total':
                        os.remove(i)
    print('用时:'+ str(end-start)+'s')
