import os
from cgi import log

import requests
# import了getconfig，在这个时候，我们的目录地址是api,本来应该是要读取common上的
import yaml

from api.base_api import BaseApi
from common.get_config import GetConfig
from common.get_log import Logs


class GetToken(BaseApi):
    log=Logs().get_log()
    config=GetConfig()
    # 通过配置文件拿到secret
    contact_secret=config.get_value("wework","contact_secret")
    id=config.get_value("wework","id")
    # secret="x0Bur6bjg9ZtNhs_qYDcDlxkB1EoBB-L4FsFmfX2Dug"
    # 获取token值
    def get_token(self,secret):
        id="ww630f49269e06f865"
        url="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params=f"corpid={id}&corpsecret={secret}"
        res= requests.get(url=url,params=params)
        return res.json()["access_token"]
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": f"corpid={self.id}&corpsecret={self.contact_secret}"
        }
        res=requests.request(**data).json()
    # pip install pyyaml
    #     file_path=os.path.join(self.BASE_PATH,"data/contact/member/member_api.yml")
    #     with open(file_path) as f:
    #         data = yaml.safe_load(f)
    #         # 需要解决一下拿出来的数据不对的问题
    #         # 需要修改这个字典
    #         data["params"]=f"corpid={self.id}&corpsecret={self.contact_secret}"
    #     res = self.send_api(data)
    #     self.log.info(res)
    #     return res["access_token"]


if __name__ == "__main__":
    a=GetToken()
    print(len(a.get_token(a.contact_secret)))
