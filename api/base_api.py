import json
import os
from string import Template
import requests
import yaml

from common.get_config import cf
from common.get_log import log


class BaseApi():
    ip=cf.get_value("env","ip")

    # 根路径基本不变，是一个常量，尽量用大写英文字母
    BASE_PATH=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 封装我们的requests的方法,传入请求的数据，返回字典类型的响应体
    def send_api(self,data:dict):
        res=requests.request(**data).json()
        log.info(f"响应值：{res}")
        return res

    # 读取yml文件,file_path是相对路径，是yaml文件的相对路径
    def load_yml(self,file_path):
        yml_path=os.path.join(self.BASE_PATH,file_path)

        with open(yml_path,encoding="utf-8") as f:
            # 这里传file_path路径问题
            data=yaml.safe_load(f)
            # 这里是一个python的数据类型，大概率就是字典、列表、集合、元祖
            return data

    # 优化api的代码，进行精简
    def send_data_api(self,p_data,yaml_path,sub):
        request_data = self.template(yaml_path, p_data, sub)
        # 对我们的request_data进行处理就好了
        # 写死的方法,拿到json的dict
        log.error(f"查看try之前的请求参数：{request_data}")
        try:
            # 当出现异常，后面的代码不跑
            json_request_data=request_data["json"]
            log.error("是否有一次是运行下去的")
            # 提取json字典中所有的key值
            for key in json_request_data.keys():
                # 当value的值与"None"相等的时候
                if json_request_data[key]== "None":
                    # 为什么"None"=="None",字符串的内存地址是相等的,说法不太对
                    log.error("是否触发修改None的代码")
                    json_request_data[key]=None
        except:
            # try引发的异常会在except中运行
            pass
        log.info(request_data)
        res = self.send_api(request_data)
        return res

    # 定义一个模板技术的方法，把yml文件中的$变量，都变成我们需要的变量
    # 要传什么参数先不管，返回一个字典类型的请求
    # file_path是yml文件的相对路径
    # p_data是对$变量，传的字典类型值
    # def template(self,file_path,p_data):
    #     dict_data=self.load_yml(file_path)
    #     str_data=str(dict_data)
    #     request_data=Template(str_data).substitute(p_data)
    #     return request_data


    # def template(self,file_path,p_data):
    #     # 得读取yaml文件，先弄好yml文件相对路径
    #     yml_path=os.path.join(self.BASE_PATH,file_path)
    #
    #     with open(yml_path) as f:
    #         # f是一个文件流，要变成字符串，写成f.read()就变成字符串了
    #         str_request=Template(f.read()).substitute(p_data)
    #         # 还是得把字符串类型改变成为字典类型
    #         # 这个字符串是不是感觉就是一个yml的字符串类型呀
    #         yaml_data=yaml.safe_dump(str_request)
    #         request_data=yaml.safe_load(yaml_data)
    #     # return request_data
    #     return request_data

    # def template(self,file_path,p_data,sub=None):
    #     # 得读取yaml文件，先弄好yml文件相对路径
    #     yml_path=os.path.join(self.BASE_PATH,file_path)
    #     with open(yml_path) as f:
    #         # f.read()就是一个字符串，Template需要传一个字符串，满足需求
    #         # p_data就是我们要改变$变量，传的是一个字典类型
    #         # Template(f.read()).substitute(p_data) 返回的是一个yml类型的字符串
    #         # yaml.safe_load(yml类型的字符串)
    #         request_data=yaml.safe_load(Template(f.read()).substitute(p_data))
    #     return request_data

    def template(self,file_path,p_data,sub=None):
        # 得读取yaml文件，先弄好yml文件相对路径
        yml_path=os.path.join(self.BASE_PATH,file_path)
        with open(yml_path) as f:
            if sub == None:
            # f.read()就是一个字符串，Template需要传一个字符串，满足需求
            # p_data就是我们要改变$变量，传的是一个字典类型
            # Template(f.read()).substitute(p_data) 返回的是一个yml类型的字符串
            # yaml.safe_load(yml类型的字符串)
                request_data=yaml.safe_load(Template(f.read()).substitute(p_data))
            else:
                # 先读取整个yml文件的数据
                yml_data=self.load_yml(file_path)
                # 拿到sub的第二级目录
                sub_data=yml_data[sub]
                # 转化成str类型,用yaml.dump
                sub_str=yaml.dump(sub_data)
                # 用模板技术转化变量
                sub_str=Template(sub_str).substitute(p_data)
                # 要把str转化成dict
                request_data=yaml.safe_load(sub_str)
                return request_data
            # request_data=yaml.safe_load(Template(str(self.load_yml(file_path)[sub])).substitute(p_data))

        return request_data
    # @classmethod
    # def template(cls, file_path, data, sub=None):
    #     yml_path = os.path.join(cls.BASE_PATH, file_path)
    #     """
    #     使用模板技术，把yml文件中的变量进行二次转化，是本框架的yml文件的技术基础
    #     :param path: 模板技术输入yml文件相对路径
    #     :param data: data是需要修改的模板变量的字典类型
    #     :param sub: sub是对yml的数据进行二次提取，等于是一个大字典，再提取下一层的小字典，为了让一个yml文件可以有多个接口数据
    #     :return:
    #     """
    #     with open(yml_path, encoding="utf-8") as f:
    #         if sub is None:
    #             '''
    #             不需要对数据进行二次提取，Template(f.read()).substitute(data)先替换变量
    #             yaml.safe_load把yml格式的字符串变成dict类型返回
    #             '''
    #             return yaml.safe_load(Template(f.read()).substitute(data))
    #         else:
    #             '''
    #             由于Template需要替换全部的变量，有漏的就会报错，先写Template(f.read()).substitute(data)
    #             就会报错，data只对sub下一层的数据改，并没有改其他层的数据，肯定会报错
    #             需要先yaml.safe_load(f)[sub]提取到下一层的数据，但由于是dict
    #             要通过yaml.dump转化成yml格式的字符串，经过Template来改变变量，最后在yaml.safe_load转化成dict
    #             '''
    #             return yaml.safe_load(Template(yaml.dump(yaml.safe_load(f)[sub])).substitute(data))
    #             # 错误的写法：return yaml.safe_load(Template(f.read()).substitute(data))



if __name__=="__main__":
    a=BaseApi()
    # print(a.BASE_PATH)
    # # print(a.load_yml("data/contact/member/add_member.yml"))
    # name="tong"
    # # print(a.template("data/contact/member/a.yml",{"name":name}))
    # # print(type(a.template("data/contact/member/a.yml",{"name":name})))
    # request_str=a.template("data/contact/member/a.yml",{"name":name})
    # print(request_str)
    # print(type(request_str))
    # # print(request_dict,type(request_dict))
    # a=BaseApi()
    # 先读取整个数据
    # data_dict=a.load_yml("data/contact/member/member_api.yml")
    # print(data_dict)
    # 通过sub提取二级目录（字典）
    # delete_data=str(data_dict["delete"])
    #
    p_data={"token":"123","userid":456}
    # 用模板工具去转化，获得新的请求数据，字符串
    # data=Template(delete_data).substitute(p_data)
    # print(data)
    # a.template("data/contact/member/member_api.yml",p_data)
    c=(a.template("data/contact/member/member_api.yml", p_data, "delete"))
    print(type(c))




