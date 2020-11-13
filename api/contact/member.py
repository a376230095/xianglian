
# 类相当于大的api模块
import yaml

from api.base_api import BaseApi
from api.get_token import GetToken
from common.get_config import cf


class Member(BaseApi):
    # 通过配置文件拿
    cf.get_value("wework","contact_secret")

    token=GetToken().get_token()

    # 方法就是指每一个具体业务的api
    # 增加联系人
    # 这个函数需要传请求的参数，获取响应
    def add_member(self,userid,name,mobile,department):
        # 1.读取我们的yml文件，读取add_mameber.yml的请求数据
        # data=self.load_yml("data/contact/member/add_member.yml")
        # 2.对拿到的字典请求的data进行变量的二次处理，需要用到Tamplate技术
        p_data={"userid":userid,"name":name,"mobile":mobile,"department":department}
        request_data=self.template("data/contact/member/add_member.yml",p_data)

        return "响应"

    # 删除联系人
    def delete_member(self):
        pass