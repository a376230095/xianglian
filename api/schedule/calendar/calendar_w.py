#-*- coding: utf-8 -*-
from api.base_api import BaseApi
from api.get_token import GetToken
from common.get_config import cf
from common.use_mysql import mysql


class CalendarW(BaseApi):
    # 由于日程的secret是另一个秘钥，需要在配置文件中新建一个，并在这里获取，作为测试用，测试完需要屏蔽他
    schedule_secret=cf.get_value("wework","schedule")
    token=GetToken().get_token(schedule_secret)

    # 作为api_yml的公共属性，因为add、get、delete、edit都需要用到这个路径，所以提取出来
    api_yml_path="data/schedule/calendar/calendar_api.yml"

    # 通过数据库获取cal_id，这样就不用依赖add方法去获取了，如果使用add方法，等于我们一直都在对一个id进行删减
    def get_cal_id_list(self):
        # 通过select获取cai_id元祖
        cal_id_tuple = mysql.select("select cal_id from cal_id where userid='calendar'")
        # 把cal_id的元祖转化成为列表的方式
        cal_id_list = []
        for i in cal_id_tuple:
            cal_id_list.append(i[0])
        return cal_id_list

    # 获取cal_id，通过列表获取
    def get_cal_id(self,index):
        return self.get_cal_id_list()[index]


    def add_cal(self,token,organizer,readonly,set_as_default,summary,color,description):
        p_data={"token":token,"ip":self.ip,"organizer":organizer,"readonly":readonly
                ,"set_as_default":set_as_default,"summary":summary,"color":color
            ,"description":description}
        # 发送请求，获得响应
        res=self.send_data_api(p_data,self.api_yml_path,"add")
        # 去保存一下cal_id，当api执行成功的时候，才去把cal_id和userid都存到数据库中
        if res["errcode"]==0:
            cal_id=res["cal_id"]
            mysql.insert(f"insert into cal_id(userid,cal_id) values('{organizer}','{cal_id}')")
        return res

    # 由于获取日历需要用到cal_id_list，我们又不想直接拿，想直接拿到某一个cal_id，想实现这个功能
    def get_cal(self,token,index):
        # 获取cal_id
        cal_id=self.get_cal_id(index)
        # 把cal_id转化成为list，因为cal_id_list是要传一个list
        cal_id_list=[]
        cal_id_list.append(cal_id)
        p_data={"token":token,"ip":self.ip,"cal_id_list":cal_id_list}
        res = self.send_data_api(p_data, self.api_yml_path, "get")
        return res


if __name__=="__main__":
    # 读取的数据是一个元祖，需要转化成列表

        # print(i[0])
    # print(cal_id_list)
    # first=cal_id_list[0]
    # print(first)
    a=CalendarW()
    # print(a.get_cal_id_list())
    print(a.get_cal(a.token,0))
    # print(a.add_cal(a.token,"calendar",1,1,"tongtong","0000FF","tongtongtong"))
    # a="abc"
    # b=[]
    # b.append(a)
    # b=list(a)
    # print(b)



