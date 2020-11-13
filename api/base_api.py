import json
import os
from string import Template

import requests
import yaml


class BaseApi():
    # 根路径基本不变，是一个常量，尽量用大写英文字母
    BASE_PATH=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 封装我们的requests的方法,传入请求的数据，返回字典类型的响应体
    def send_api(self,data:dict):
        res=requests.request(**data).json()
        return res

    # 读取yml文件,file_path是相对路径，是yaml文件的相对路径
    def load_yml(self,file_path):
        yml_path=os.path.join(self.BASE_PATH,file_path)

        with open(yml_path) as f:
            # 这里传file_path路径问题
            data=yaml.safe_load(f)
            # 这里是一个python的数据类型，大概率就是字典、列表、集合、元祖
            return data

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

    def template(self,file_path,p_data):
        # 得读取yaml文件，先弄好yml文件相对路径
        yml_path=os.path.join(self.BASE_PATH,file_path)
        with open(yml_path) as f:
            # f.read()就是一个字符串，Template需要传一个字符串，满足需求
            # p_data就是我们要改变$变量，传的是一个字典类型
            # Template(f.read()).substitute(p_data) 返回的是一个yml类型的字符串
            # yaml.safe_load(yml类型的字符串)
            request_data=yaml.safe_load(Template(f.read()).substitute(p_data))
        return request_data



if __name__=="__main__":
    a=BaseApi()
    # print(a.BASE_PATH)
    # print(a.load_yml("data/contact/member/add_member.yml"))
    name="tong"
    # print(a.template("data/contact/member/a.yml",{"name":name}))
    # print(type(a.template("data/contact/member/a.yml",{"name":name})))
    request_str=a.template("data/contact/member/a.yml",{"name":name})
    print(request_str)
    print(type(request_str))
    # print(request_dict,type(request_dict))

