from api.contact.member import Member


class TestMember():
    # 初始化member对象，获取到了token值
    member=Member()

    def test_add_member(self):
        # 1.获取access_token
        # 2.添加联系人
        res = self.member.add_member("zhangsan","张三","+86 13800000000",[1,2])
        assert res["errcode"] == 60104
        assert  "mobile existed" in res["errmsg"]


    def test_delete_member(self):
        # 1.获取access_token
        # 2.添加联系人
        res =self.member.delete_member("abc")
        assert res["errcode"] == 60111
        assert  "userid not found" in res["errmsg"]

