import pandas as pd
import os

# 读取文件，处理掉非进出站操作产生的数据

all_data = pd.DataFrame()
num = 0
for root,dirs,files in os.walk(r'H:\工作\!!!香河\excel_公交\路径数据\2019-12-14-周六',topdown=False):
    # print(files)
    for i in files:
        print(i)
        chepaihao = i.split('-')[0]
        print(chepaihao)
        # 读取文件
        df = pd.read_excel(r'H:\工作\!!!香河\excel_公交\路径数据\2019-12-14-周六/{}'.format(i))
        # print(df)
        # 把 其他信息 == NaN的删去
        withoutNaN = df[df['其他信息'].notnull()]
        withoutNaN['车牌号'] = chepaihao
        # print(withoutNaN)
        # 选出有需要的列[[]] 变成新的DataFrame
        newpd = withoutNaN[['线路名称','Gps时间','速度','其他信息','车牌号']]
        # print(newpd)
        # print(newpd[:20])
        # [:,2]选取第三列gpstime（第0列为index）
        # timeSeries = withoutNaN.iloc[:,2]
        # print(timeSeries)
        num +=1
        print(num)

        writer = pd.ExcelWriter(r'H:\工作\!!!香河\excel_公交\路径数据\2019-12-14-周六_简化\\'+ chepaihao +'_简化.xlsx')
        newpd.to_excel(writer,'AllData')
        writer.save()
        print('finished')