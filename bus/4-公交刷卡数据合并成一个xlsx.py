import os
import pandas as pd
from multiprocessing import Process

pd.set_option('display.width',None)
for root,dir,files in os.walk(r'H:\工作\!!!香河\excel_公交\消费交易明细查询-20210419'):
    lst1 = [root+'\\'+i for i in files[0:12]]
    lst2 = [root+'\\'+i for i in files[12:24]]
    lst3 = [root+'\\'+i for i in files[24:36]]
# print(lst1)
def fun(lst):
    alldate = pd.DataFrame()
    for i in lst:
        df = pd.read_excel(i)
        alldate = alldate.append(df)

    alldate = alldate[['交易类型','所属线路','车牌号','卡号','卡类型','交易计数器','New交易时间','NewLocation']]
    # writer = pd.ExcelWriter(r'H:\工作\!!!香河\excel_公交\消费交易明细查询-20210419\\'+lst[0].split('\\')[-1].replace('1.','合并.'))
    # print('done')
    # print(alldate.head())
    # alldate.to_excel(writer,'ALLdate')
    alldate.to_excel(r'H:\工作\!!!香河\excel_公交\消费交易明细查询-20210419\\'+lst[0].split('\\')[-1].replace('1.','合并.'))


if __name__ == '__main__':

    x1 = Process(target=fun,args=(lst1,))
    x2 = Process(target=fun,args=(lst2,))
    x3 = Process(target=fun,args=(lst3,))

    x1.start()
    x2.start()
    x3.start()
