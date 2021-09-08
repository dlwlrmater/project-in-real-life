import time
import pandas as pd
import pymysql
import os
import math
import datetime
from multiprocessing import Process


# 结果在 H:\工作\!!!香河\excel_公交\整理od\\
# 由于数据量较大拿到数据后均导入到mysql中，通过pymysql和Process多进程，提高数据处理速度
# 由于香河公交为单次刷卡
# 通过识别唯一ID，根据刷卡时间，分辨用户OD点，从时间纬度和OD点分析现状公交线路运行情况


pd.set_option('display.width',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


# 链接mysql parameter
config = dict(
    host = 'localhost',
    user = 'root',
    password = 'root',
    cursorclass = pymysql.cursors.DictCursor,
    database = '香河公交'
)

# 连接数据库
conn = pymysql.Connect(**config)
conn.autocommit(1)
cursor = conn.cursor()



def timmme(a,b):
    c1 = datetime.datetime.strptime(a,'%Y-%m-%d %H:%M:%S')
    c2 = datetime.datetime.strptime(b,'%Y-%m-%d %H:%M:%S')
    return (c2-c1).total_seconds()

# 定义func 用于多进程操作
def func(df,lst,nnn,riqi):
    # 建立统计表格 df_all
    df_all = pd.DataFrame(columns = ['卡号','位置','时间','OD'])
    # 选择 卡号 in lst 里面的行 用于分12组
    df1 = df[df['卡号'].isin(lst)]
    for i in lst:
        # 根据前后排序筛选O,D
        num,num2 = 0,-1
        # 新建循环内统计表格 df_all1
        df_all1 = pd.DataFrame(columns=['卡号', '位置', '时间', 'OD'])
        # 选择lst内相对应的卡号 准备筛选
        df2 = df1[df1['卡号'] == i]
        # 添加的第一行为O点
        df_all1 = df_all1.append({'卡号': df2.iloc[0]['卡号'], '位置': df2.iloc[0]['NewLocation'], '时间': df2.iloc[0]['New交易时间'], 'OD': 'O'},ignore_index=True)
        # 从第二行开始筛选 如果满足 1.indexer not out-of-bounds 2.和前一个刷卡时间间隔在30s内 3.前后上车点名称一致 这三个条件 加到df_all2
        while num <= len(df2) - 2 and timmme(df2.iloc[num]['New交易时间'], df2.iloc[num + 1]['New交易时间']) < 30 and df2.iloc[num]['NewLocation'] == df2.iloc[num + 1]['NewLocation']:
            df_all1 = df_all1.append({'卡号': df2.iloc[num + 1]['卡号'], '位置': df2.iloc[num + 1]['NewLocation'],'时间': df2.iloc[num + 1]['New交易时间'], 'OD': 'O'}, ignore_index=True)
            num += 1
        # 判断 df整体最后一个值['New交易时间'] 和df_all2最后一个的['New交易时间'] 是否一样 如果不一样继续添加D点
        if df_all1.iloc[-1]['时间'] != df2.iloc[-1]['New交易时间']:
            # 添加df最后一个值为d点
            df_all1 = df_all1.append({'卡号': df2.iloc[-1]['卡号'], '位置': df2.iloc[-1]['NewLocation'], '时间': df2.iloc[-1]['New交易时间'], 'OD': 'D'},ignore_index=True)
            # 同上 从倒数第二个值开始筛选 如果满足 1.indexer not out-of-bounds 2.和前一个刷卡时间间隔在30s内 3.前后上车点名称一致 这三个条件 加到df_all2
            while num2 > -len(df2) + 1 and timmme(df2.iloc[num2 - 1]['New交易时间'], df2.iloc[num2]['New交易时间']) < 30 and df2.iloc[num2]['NewLocation'] == df2.iloc[num2 - 1]['NewLocation']:
                df_all1 = df_all1.append({'卡号': df2.iloc[num2 - 1]['卡号'], '位置': df2.iloc[num2 - 1]['NewLocation'],'时间': df2.iloc[num2 - 1]['New交易时间'], 'OD': 'D'}, ignore_index=True)
                num2 -= 1
        # 所有list分项结果合并到df_all
        df_all = df_all.append(df_all1)
    # df_all重新设置index,根据卡号和时间 升序排序
    df_all = df_all.reset_index(drop='index').sort_values(by=['卡号','时间'],ascending=True)
    # 输出结果
    return df_all.to_excel(r'H:\工作\!!!香河\excel_公交\整理od\\'+riqi+'\\'+riqi+'_'+nnn+'.xlsx')
    # return df_all


if __name__ == '__main__':
    s = time.time()
    # 1.读取卡号出现次数>=2的记录 
    sql_ = "SELECT * FROM date20191218 WHERE `卡号` in (SELECT 卡号 from date20191218 GROUP BY `卡号` HAVING COUNT(`卡号`) >= 2) ORDER BY `卡号` asc,`New交易时间` asc"
    df_data = pd.read_sql(sql_, conn)
    # 2.移除f1行(原index)
    df_data = df_data.drop(columns='f1')
    # 3.查看所有unique卡号 用于之后分组
    lst = list(df_data['卡号'].values)
    # print(len(set(lst)))
    # 4.卡号去重
    lst1 = []
    for i in lst:
        # 去除\xa0 为不间断空白符 不删除是因为后续df查询
        # i = "".join(i.split())
        if i not in lst1:
            lst1.append(i)

    # 12个cpu 平均每个处理数量 向上取整
    avgg = math.ceil(len(lst1) / 12)
    # print(avgg)

    # 根据平均数处理lst 变成由12个小lst组成的lst
    lst2 = []
    for i in range(0, len(lst1), avgg):
        lst2.append(lst1[i:i + avgg])

    # 多进程启动！
    df1 = lst2[0]
    df2 = lst2[1]
    df3 = lst2[2]
    df4 = lst2[3]
    df5 = lst2[4]
    df6 = lst2[5]
    df7 = lst2[6]
    df8 = lst2[7]
    df9 = lst2[8]
    df10 = lst2[9]
    df11 = lst2[10]
    df12 = lst2[11]

    p1 = Process(target=func,args=(df_data,df1,'1','2019-12-18',))
    p2 = Process(target=func,args=(df_data,df2,'2','2019-12-18',))
    p3 = Process(target=func,args=(df_data,df3,'3','2019-12-18',))
    p4 = Process(target=func,args=(df_data,df4,'4','2019-12-18',))
    p5 = Process(target=func,args=(df_data,df5,'5','2019-12-18',))
    p6 = Process(target=func,args=(df_data,df6,'6','2019-12-18',))
    p7 = Process(target=func,args=(df_data,df7,'7','2019-12-18',))
    p8 = Process(target=func,args=(df_data,df8,'8','2019-12-18',))
    p9 = Process(target=func,args=(df_data,df9,'9','2019-12-18',))
    p10 = Process(target=func,args=(df_data,df10,'10','2019-12-18',))
    p11 = Process(target=func,args=(df_data,df11,'11','2019-12-18',))
    p12 = Process(target=func,args=(df_data,df12,'12','2019-12-18',))

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

    e = time.time()
    print(e-s)
    # a = func(df_data,lst2[0])
    # print(a)








# df_all = pd.DataFrame(columns = ['卡号','位置','时间','OD'])
# df1 = df_data[df_data['卡号'].isin(lst)]
# df2 = df1[df1['卡号'] == '0654000101000087 ']
# print(df2)
# # print(df2.iloc[0])
# num = 0
# num2 = -1
# df_all = df_all.append({'卡号': df2.iloc[0]['卡号'], '位置': df2.iloc[0]['NewLocation'],'时间':df2.iloc[0]['New交易时间'], 'OD': 'O'},ignore_index=True)
# while num <= len(df2)-2 and timmme(df2.iloc[num]['New交易时间'],df2.iloc[num+1]['New交易时间']) <30 and df2.iloc[num]['NewLocation'] == df2.iloc[num+1]['NewLocation'] :
#     df_all = df_all.append({'卡号': df2.iloc[num+1]['卡号'], '位置': df2.iloc[num+1]['NewLocation'],'时间':df2.iloc[num+1]['New交易时间'], 'OD': 'O'},ignore_index=True)
#     print(num)
#     num +=1
# # 添加最后一行
# if df_all.iloc[-1]['时间'] != df2.iloc[-1]['New交易时间']:
#     df_all = df_all.append({'卡号': df2.iloc[-1]['卡号'], '位置': df2.iloc[-1]['NewLocation'],'时间':df2.iloc[-1]['New交易时间'], 'OD': 'D'},ignore_index=True)
#
#     print(num2)
#     print(num2 > -len(df2) + 1)
#     print(timmme(df2.iloc[num2]['New交易时间'],df2.iloc[num2-1]['New交易时间']) <30)
#     print(df2.iloc[num2]['NewLocation'] == df2.iloc[num2-1]['NewLocation'])
#
#     while num2 > -len(df2) +1 and timmme(df2.iloc[num2-1]['New交易时间'],df2.iloc[num2]['New交易时间']) <30 and df2.iloc[num2]['NewLocation'] == df2.iloc[num2-1]['NewLocation']:
#         df_all = df_all.append({'卡号': df2.iloc[num2 - 1]['卡号'], '位置': df2.iloc[num2 - 1]['NewLocation'],'时间':df2.iloc[num2-1]['New交易时间'], 'OD': 'D'},ignore_index=True)
#         num2 -=1
# print(df_all)

