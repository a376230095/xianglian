import pytest

from api.contact.member import Member
from api.get_token import GetToken
from common.get_config import cf
from common.get_log import log


class TestMember():
    # 初始化member对象，获取到了token值
    member = Member()
    ids = ["电话号码重复", "userid重复", "name重复"]

    # 拿到我们的数据，ids的标题数据，参数化用的数据
    delete_data = member.load_yml("data/contact/member/member_para.yml")
    delete_data = delete_data["delete"]
    delete_ids = delete_data["ids"]
    delete_para = delete_data["data"]

    add_data = member.load_yml("data/contact/member/member_para.yml")["add"]
    add_ids = add_data["ids"]
    add_para = add_data["data"]

    # def setup(self):
    #     # 增加联系人之前需要删除联系人
    #     # 由于setup方法作用对象是每一个用例，这样可能会出现一些问题，或者是一些冗余，因为我们的删除联系人是不需要用这个setup的方法的
    #     # 不灵活
    #     pass
    #
    # def teardown(self):



    @pytest.mark.parametrize(("userid,name,mobile,department,errcode,errmsg"),add_para,ids=add_ids)
    def test_add_member(self, access_token, userid, name, mobile, department, errcode, errmsg,add):
        log.info("--------------执行增加联系人--------------")
        # 1.获取access_token
        # 2.添加联系人
        res = self.member.add_member(access_token, userid, name, mobile, department)
        log.info("--------------结束增加联系人--------------")
        assert errcode == res["errcode"]
        assert errmsg in res["errmsg"]

    @pytest.mark.parametrize(("userid,errcode,errmsg"), delete_para, ids=delete_ids)
    def test_delete_member(self, access_token, userid, errcode, errmsg,delete):
        log.info("--------------执行删除联系人--------------")
        # 1.获取access_token
        # 2.添加联系人
        res = self.member.delete_member(access_token, userid)
        log.info("--------------结束删除联系人--------------")
        assert errcode == res["errcode"]
        assert errmsg in res["errmsg"]
