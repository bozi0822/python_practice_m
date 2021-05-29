# coding:utf-8

import requests
import json
import time
import random

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    'content-type': "application/json"
}

all = [
    {"groupArea": "禅城区",
     "groupStreets": {
         "石湾街道", "张槎街道", "祖庙街道", "南庄镇"
     }},
    {"groupArea": "南海区",
     "groupStreets": {
         "桂城街道", "丹灶镇", "狮山镇", "大沥镇", "里水镇"
     }},
    {"groupArea": "顺德区",
     "groupStreets": {
         "大良街道", "伦教街道", "北滘镇", "陈村镇"
     }},
]

url2 = 'https://fsservice.wjj.foshan.gov.cn/fw2/foying/wechatpublic/wx/userBooking/getScheduleByDate'
url1 = 'https://fsservice.wjj.foshan.gov.cn/fw2/foying/wechatpublic/wx/userBooking/getOrganizeByGroupArea'


def open_uri(groupArea, groupStreet):
    body = {
        "groupArea": groupArea,
        "groupStreet": groupStreet
    }
    res = requests.post(url1, headers=header, data=json.dumps(body))
    # print(res.text)
    data = res.text
    resList = []
    #################################################################################################################################
    # data = '{"ResCode":"100","ResMsg":"获取机构列表成功","entityList":[{"address":"禅城区石湾镇街道惠景路8号城南社区卫生服务中心","allowOrderUserType":"au1","id":"1e3a4e4a3f6542ef888e75678d455f5f1617156071169","organizeEnCode":"4406040431","organizeName":"石湾镇街道城南社区卫生服务中心预防接种门诊","showFlag":"1","telephone":""},{"address":"佛山市禅城区绿景西路10号50号铺","allowOrderUserType":"au1","id":"2d1fc3a0991a4c7ca75a2a8d954730061617154824217","organizeEnCode":"4406040434","organizeName":"石湾镇街道番村社区卫生服务站临时接种点","showFlag":"0","telephone":""},{"address":"佛山市禅城区奇槎村奇槎新基42号","allowOrderUserType":"au1","id":"424c9471da194d53b77d36006f7435621618800142086","organizeEnCode":"4406040405","organizeName":"禅城区人民医院奇槎新冠临时接种点","showFlag":"0","telephone":""},{"address":"佛山市第一人民医院健康管理中心3号楼1楼大堂","allowOrderUserType":"au1,au2","id":"501977ac24ab436f8b2c4bcc6cf2b9601617249299578","organizeEnCode":"4406040130","organizeName":"佛山市第一人民医院新冠疫苗接种点","showFlag":"0","telephone":""},{"address":"石湾镇街道澜石前进路88号澜石码头","allowOrderUserType":"au1","id":"56c1e81068ae4227817a0ff4574e2e3c1617155817357","organizeEnCode":"4406040433","organizeName":"佛山市禅城区石湾镇街道大型接种点","showFlag":"0","telephone":""},{"address":"禅城区石湾镇街道汾江南路9号一楼","allowOrderUserType":"au1","id":"6bce5464beda48cbb4a691a1d25f4cad1616920840275","organizeEnCode":"4406040401","organizeName":"禅城区中心医院里水社区卫生服务站新冠接种门诊","showFlag":"0","telephone":"83385330"},{"address":"佛山市禅城区文华中路72号","allowOrderUserType":"au1","id":"8d833ddbd4304f1ba83a3ee3a6c3fa861620958775430","organizeEnCode":"4406040403","organizeName":"汉德（佛山）骨科医院新冠疫苗临时接种点","showFlag":"0","telephone":""},{"address":"禅城区石湾镇街道三友南路3号6号楼儿保园","allowOrderUserType":"au1","id":"8f12e1de035a4ee18e645815d2f1c3151616920568069","organizeEnCode":"4406040430","organizeName":"禅城区中心医院预防接种门诊","showFlag":"1","telephone":"82778663"},{"address":"石湾镇街道前进路1号澜石小学旁（六楼）","allowOrderUserType":"au1","id":"a660b4b013394f1d958495c664374e871616920000674","organizeEnCode":"4406040436","organizeName":"石湾镇街道社区卫生服务中心新冠固定接种点","showFlag":"0","telephone":""},{"address":"禅城区石湾镇街道前进路1号澜石小学旁（三楼）","allowOrderUserType":"au1","id":"bd66900acd2348378be06fd13f16bc731616919497529","organizeEnCode":"4406040432","organizeName":"石湾镇街道社区卫生服务中心预防接种门诊","showFlag":"0","telephone":""},{"address":"佛山市禅城区深村大道深村社区卫生服务站旁","allowOrderUserType":"au1","id":"e836b9aeb52e4acca41160ad0ce0130c1617156391382","organizeEnCode":"4406040445","organizeName":"石湾镇街道深村社区卫生服务站怡康楼","showFlag":"0","telephone":""}]}'
    info_dic = json.loads(data)
    print("\n")
    print("==========", groupStreet, "===============")
    for item in info_dic["entityList"]:
        show_flag = item["showFlag"]
        organizeName = item['organizeName']
        # print(organizeName + " - 无号")
        if (show_flag == '1'):
            # print('===============================================================================' + item['organizeName'] + ' - ' + item['address'] + ' 有号')
            resList.append(item['id'])
    return resList


def open_uri2(scheduleDate, baseOrganizeID):
    body = {
        "scheduleDate": scheduleDate,
        "baseOrganizeID": baseOrganizeID
    }
    res = requests.post(url2, headers=header, data=json.dumps(body))
    # print(res.text)
    data = res.text
    ########################################################################################################################################
    # data = '{"ResCode":"100","ResMsg":"获取排班信息成功","entityList":[{"beginTimeStr":"14:30:00","count":300,"endTimeStr":"15:30:00","scheduleID":"9086ee28830d43d5866362d4f98349df1622176400468","vaccineProducer":"北京生物（含长春、兰州和成都）"},{"beginTimeStr":"15:30:00","count":0,"endTimeStr":"16:30:00","scheduleID":"e68e3605c8314a20a22792c77851130a1622176430593","vaccineProducer":"北京生物（含长春、兰州和成都）"}]}'
    info_dic = json.loads(data)
    for item in info_dic["entityList"]:
        count = item["count"]
        vaccineProducer = item["vaccineProducer"]
        countInt = int(count)
        if (countInt > 0):
            print(vaccineProducer + ' ==剩余数量：' + str(count))


if __name__ == '__main__':
    today = time.strftime("%Y-%m-%d", time.localtime())

    resList = []
    for i in range(2):
        for item in all:
            groupArea = item.get("groupArea")
            groupStreets = item.get("groupStreets")
            print("\n")
            print("\n")
            print(
                "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" + '\n' +
                "+++++++++++++++++++++++++++++++++++++++++++++++++++", groupArea,
                "++++++++++++++++++++++++++++++++++++++++++++++" + '\n' +
                "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
            )
            for groupStreet in groupStreets:
                resList = open_uri(groupArea, groupStreet)
                random_num = random.randint(0, 3)
                time.sleep(random_num)
                if (resList.__len__() > 0):
                    print('watchOUT!!!!')
                    for res in resList:
                        print(groupArea, groupStreet)
                        open_uri2(today, res)
