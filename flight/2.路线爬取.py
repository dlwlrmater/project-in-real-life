import requests
import pandas as pd
import time
import datetime
import csv

headers = {

    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.740261823.1567647866; _gid=GA1.2.387000010.1567647866; PHPSESSID=gm2q6h7qh066i7bdak72rkp2p4; Hm_lvt_de76267abe273488e66f73620a0a2118=1567647865,1567674394,1567730271; _gat_gtag_UA_93103382_2=1; Hm_lpvt_de76267abe273488e66f73620a0a2118=1567750194',
    'Host': 'data.variflight.com',
    'Referer': 'https://data.variflight.com/profiles/Airports/PEK/route',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
            }
url = 'https://data.variflight.com/profiles/Airportsroute/routeDetail'
# req = request.Request(url=url,headers=headers)
# rsp = request.urlopen(req)
# html = rsp.read().decode()
# print(html)
wendang = csv.reader(open(r'D:\!!python result\Varifight\机场代码2.csv','r',encoding='UTF-8'))
T= []
for X in wendang:
    code = X[0]
    T.append(code)
T = T[1:]
start = datetime.datetime.now()
for R in T:


    data={
        'start': '2019-03-31',
        'end': '2019-10-26',
        'airport': R,
        'airlines': 'total'
    }
    req = requests.post(url=url,headers=headers,data=data)
    r=req.json()
    print(r)
    message_ = r['message']
    try:
        if message_ == '查询成功':
            flights = []
            seat = []
            ftype = []
            desc = []
            seatRat = []
            flightsRat = []
            stopMark = []
            type = []

            # 一级分类
            z = r['data']
            if 'inland' in z.keys():
                inland_ = z['inland']
                if 'isstop' in inland_.keys():
                    # inland
                    inland_isstop_ = inland_['isstop']
                    inland_isstop_route_ = inland_isstop_['route']
                    # inland_isstop code
                    for index_inland in range(len(inland_isstop_route_)):
                        inland_isstop_route_flights_ = inland_isstop_route_[index_inland]['flights']
                        flights.append(inland_isstop_route_flights_)
                        inland_isstop_route_seat_ = inland_isstop_route_[index_inland]['seat']
                        seat.append(inland_isstop_route_seat_)
                        inland_isstop_route_ftype_ = inland_isstop_route_[index_inland]['ftype']
                        ftype.append(inland_isstop_route_ftype_)
                        inland_isstop_route_desc_ = inland_isstop_route_[index_inland]['desc']
                        desc.append(inland_isstop_route_desc_)
                        inland_isstop_route_seatRat_ = inland_isstop_route_[index_inland]['seatRat']
                        seatRat.append(inland_isstop_route_seatRat_)
                        inland_isstop_route_flightsRat_ = inland_isstop_route_[index_inland]['flightsRat']
                        flightsRat.append(inland_isstop_route_flightsRat_)
                        inland_isstop_route_stopMark_ = inland_isstop_route_[index_inland]['stopMark']
                        stopMark.append(inland_isstop_route_stopMark_)
                        inland_isstop_type_ = 'inland_isstop'
                        type.append(inland_isstop_type_)
                if 'direct' in inland_.keys():
                    inland_direct_ = inland_['direct']
                    inland_direct_route_ = inland_direct_['route']
                    # inland_direct code
                    for index_inland in range(len(inland_direct_route_)):
                        inland_direct_route_flights_ = inland_direct_route_[index_inland]['flights']
                        flights.append(inland_direct_route_flights_)
                        inland_direct_route_seat_ = inland_direct_route_[index_inland]['seat']
                        seat.append(inland_direct_route_seat_)
                        inland_direct_route_ftype_ = inland_direct_route_[index_inland]['ftype']
                        ftype.append(inland_direct_route_ftype_)
                        inland_direct_route_desc_ = inland_direct_route_[index_inland]['desc']
                        desc.append(inland_direct_route_desc_)
                        inland_direct_route_seatRat_ = inland_direct_route_[index_inland]['seatRat']
                        seatRat.append(inland_direct_route_seatRat_)
                        inland_direct_route_flightsRat_ = inland_direct_route_[index_inland]['flightsRat']
                        flightsRat.append(inland_direct_route_flightsRat_)
                        inland_direct_route_stopMark_ = inland_direct_route_[index_inland]['stopMark']
                        stopMark.append(inland_direct_route_stopMark_)
                        inland_direct_type_ = 'inland_direct'
                        type.append(inland_direct_type_)
                else:
                    print('inland少嗷')
                    pass
            if 'internation' in z.keys():
                internation_ = z['internation']
                if 'isstop' in internation_.keys():
                    # internation
                    internation_isstop_ = internation_['isstop']
                    internation_isstop_route_ = internation_isstop_['route']
                    # internation_isstop code
                    for index_internation in range(len(internation_isstop_route_)):
                        internation_isstop_route_flights_ = internation_isstop_route_[index_internation]['flights']
                        flights.append(internation_isstop_route_flights_)
                        internation_isstop_route_seat_ = internation_isstop_route_[index_internation]['seat']
                        seat.append(internation_isstop_route_seat_)
                        internation_isstop_route_ftype_ = internation_isstop_route_[index_internation]['ftype']
                        ftype.append(internation_isstop_route_ftype_)
                        internation_isstop_route_desc_ = internation_isstop_route_[index_internation]['desc']
                        desc.append(internation_isstop_route_desc_)
                        internation_isstop_route_seatRat_ = internation_isstop_route_[index_internation]['seatRat']
                        seatRat.append(internation_isstop_route_seatRat_)
                        internation_isstop_route_flightsRat_ = internation_isstop_route_[index_internation]['flightsRat']
                        flightsRat.append(internation_isstop_route_flightsRat_)
                        internation_isstop_route_stopMark_ = internation_isstop_route_[index_internation]['stopMark']
                        stopMark.append(internation_isstop_route_stopMark_)
                        internation_isstop_type_ = 'internation_isstop'
                        type.append(internation_isstop_type_)
                if 'direct' in internation_.keys():
                    internation_direct_ = internation_['direct']
                    internation_direct_route_ = internation_direct_['route']
                    # internation_direct code
                    for index_internation in range(len(internation_direct_route_)):
                        internation_direct_route_flights_ = internation_direct_route_[index_internation]['flights']
                        flights.append(internation_direct_route_flights_)
                        internation_direct_route_seat_ = internation_direct_route_[index_internation]['seat']
                        seat.append(internation_direct_route_seat_)
                        internation_direct_route_ftype_ = internation_direct_route_[index_internation]['ftype']
                        ftype.append(internation_direct_route_ftype_)
                        internation_direct_route_desc_ = internation_direct_route_[index_internation]['desc']
                        desc.append(internation_direct_route_desc_)
                        internation_direct_route_seatRat_ = internation_direct_route_[index_internation]['seatRat']
                        seatRat.append(internation_direct_route_seatRat_)
                        internation_direct_route_flightsRat_ = internation_direct_route_[index_internation]['flightsRat']
                        flightsRat.append(internation_direct_route_flightsRat_)
                        internation_direct_route_stopMark_ = internation_direct_route_[index_internation]['stopMark']
                        stopMark.append(internation_direct_route_stopMark_)
                        internation_direct_type_ = 'internation_direct'
                        type.append(internation_direct_type_)
                else:
                    print('internation少嗷')
                    pass
            if 'region' in z.keys():
                region_ = z['region']
                if 'isstop' in region_.keys():
                    # region
                    region_isstop_ = region_['isstop']
                    region_isstop_route_ = region_isstop_['route']
                    # region_isstop code
                    for index_region in range(len(region_isstop_route_)):
                        region_isstop_route_flights_ = region_isstop_route_[index_region]['flights']
                        flights.append(region_isstop_route_flights_)
                        region_isstop_route_seat_ = region_isstop_route_[index_region]['seat']
                        seat.append(region_isstop_route_seat_)
                        region_isstop_route_ftype_ = region_isstop_route_[index_region]['ftype']
                        ftype.append(region_isstop_route_ftype_)
                        region_isstop_route_desc_ = region_isstop_route_[index_region]['desc']
                        desc.append(region_isstop_route_desc_)
                        region_isstop_route_seatRat_ = region_isstop_route_[index_region]['seatRat']
                        seatRat.append(region_isstop_route_seatRat_)
                        region_isstop_route_flightsRat_ = region_isstop_route_[index_region]['flightsRat']
                        flightsRat.append(region_isstop_route_flightsRat_)
                        region_isstop_route_stopMark_ = region_isstop_route_[index_region]['stopMark']
                        stopMark.append(region_isstop_route_stopMark_)
                        region_isstop_type_ = 'region_isstop'
                        type.append(region_isstop_type_)
                if 'direct' in region_.keys():
                    region_direct_ = region_['direct']
                    region_direct_route_ = region_direct_['route']
                    # region_direct code
                    for index_region in range(len(region_direct_route_)):
                        region_direct_route_flights_ = region_direct_route_[index_region]['flights']
                        flights.append(region_direct_route_flights_)
                        region_direct_route_seat_ = region_direct_route_[index_region]['seat']
                        seat.append(region_direct_route_seat_)
                        region_direct_route_ftype_ = region_direct_route_[index_region]['ftype']
                        ftype.append(region_direct_route_ftype_)
                        region_direct_route_desc_ = region_direct_route_[index_region]['desc']
                        desc.append(region_direct_route_desc_)
                        region_direct_route_seatRat_ = region_direct_route_[index_region]['seatRat']
                        seatRat.append(region_direct_route_seatRat_)
                        region_direct_route_flightsRat_ = region_direct_route_[index_region]['flightsRat']
                        flightsRat.append(region_direct_route_flightsRat_)
                        region_direct_route_stopMark_ = region_direct_route_[index_region]['stopMark']
                        stopMark.append(region_direct_route_stopMark_)
                        region_direct_type_ = 'region_direct'
                        type.append(region_direct_type_)
                else:
                    print('region少嗷')
                    pass

            dt = pd.DataFrame({'架次':flights,'座位数':seat,'主力机型':ftype,'航线':desc,'seatRat':seatRat,'flightsRat':flightsRat,
                               'stopMark':stopMark,'type':type,'机场':R})
            mingzi = '20190905晚上'
            dt.to_csv(r'D:\!!python result\Varifight\{}.csv'.format(mingzi),mode='a',index = 0)
            print(R + '都Ok嗷')
            time.sleep(0)
        elif message_ == '您未登录或无权限':
            print('换cookie')
            break
        else:
            print(R + '我傻了,意思没数据呗就')
            # fight_Total
            # inland_fightTotal_ = inland_['fightTotal']
    except:
        print('gg')
end = datetime.datetime.now()
print('Running time: %s' % (end - start))