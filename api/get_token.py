import requests


class GetToken():
    secret="x0Bur6bjg9ZtNhs_qYDcDlxkB1EoBB-L4FsFmfX2Dug"
    # 获取token值
    def get_token(self,secret):
        id="ww630f49269e06f865"
        url="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params=f"corpid={id}&corpsecret={secret}"
        res= requests.get(url=url,params=params)
        return res.json()["access_token"]


if __name__ == "__main__":
    a=GetToken()
    print(len(a.get_token(a.secret)))
