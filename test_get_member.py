import requests
class TestGet():
    ip ="从配置文件中读取"

    def setup_class(self):
        # 获取access_token
        id = "ww630f49269e06f865"
        SECRET = "YC9RRMQcQqGNxapjoeiDIn84mCY7H-aJblz_X9X073U"
        a_url = f"https://{self.ip}/cgi-bin/gettoken?corpid={id}&corpsecret={SECRET}"
        res = requests.get(url=a_url)
        # res是一个对象，并不是一个响应体
        # res.json() json会自动帮我们转化把响应体成字典格式

        print("class")
        self.access_token = res.json()["access_token"]

    def test_get_member(self):
        # 获取联系人了
        userid="tong6"
        url="https://qyapi.weixin.qq.com/cgi-bin/user/get"
        params=f"access_token={self.access_token}&userid={userid}"
        res=requests.get(url=url,params=params).json()
        assert 0 == res["errcode"]
        assert "ok" == res["errmsg"]

    def test_delete_member(self):
        print("abc")