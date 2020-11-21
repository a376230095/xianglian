# 类相当于大的api模块
import yaml
from api.base_api import BaseApi
from api.get_token import GetToken
from common.get_config import cf
from common.get_log import log


class Member(BaseApi):
    # 通过配置文件拿
    # secret=cf.get_value("wework","contact_secret")
    #
    # token=GetToken().get_token(secret)

    # 增加联系人的api，肯定要传值的，想通过传入请求参数，获取响应
    def add_member(self,token,userid,name,mobile,department):
        # 请求数据已经放在yml文件中了，但是呢，需要把${}都变成变量，直接使用封装好的tamplate方法
        p_data={"token":token,"userid":userid,"name":name
                ,"mobile":mobile,"department":department}
        request_data=self.template("data/contact/member/member_api.yml",p_data,"add")
        # request_data["json"]["department"]=list(request_data["json"]["department"])
        log.info(request_data)
        #发送http请求，因为requests已经被封装了，直接用封装的函数
        res= self.send_api(request_data)
        #返回响应
        return res

    def delete_member(self,token,userid):
        p_data={"token":token,"userid":userid}
        request_data = self.template("data/contact/member/member_api.yml", p_data,"delete")
        log.info(request_data)
        # 发送http请求，因为requests已经被封装了，直接用封装的函数
        res = self.send_api(request_data)
        # 返回响应
        return res


if __name__=="__main__":
    a=Member()
    print(a.add_member("zhangsan","张三","+86 13800000000",[1,2]))
    # print(a.delete_member("aaa"))
    # print(a.add_member())