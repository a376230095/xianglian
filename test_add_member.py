
class TestAdd():
    def test_add_member_moblie_exist(self):
        import requests

        # 获取access_token
        id = "ww630f49269e06f865"
        SECRET = "YC9RRMQcQqGNxapjoeiDIn84mCY7H-aJblz_X9X073U"
        a_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={id}&corpsecret={SECRET}"

        res = requests.get(url=a_url)
        # res是一个对象，并不是一个响应体
        print(res.text)
        # res.json() json会自动帮我们转化把响应体成字典格式
        print(type(res.json()))

        access_token = res.json()["access_token"]

        # 创建联系人接口
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}"
        data = {
            "userid": "zhangsan",
            "name": "张三",
            "mobile": "+86 13800000000",
            "department": [1, 2]
        }
        res = requests.post(url=url, json=data)
        errmsg=res.json()["errmsg"]
        assert "mobile existed111111" in errmsg
