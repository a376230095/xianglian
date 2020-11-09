import requests


class BaseApi():
    # 封装我们的requests的方法,传入请求的数据，返回字典类型的响应体
    def send_api(self,data:dict):
        res=requests.request(**data).json()
        return res