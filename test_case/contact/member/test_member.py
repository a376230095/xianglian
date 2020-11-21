import pytest

from api.contact.member import Member
from api.get_token import GetToken
from common.get_config import cf


class TestMember():
    # 初始化member对象，获取到了token值
    member=Member()
    ids=["电话号码重复","userid重复","name重复"]

    # 拿到我们的数据，ids的标题数据，参数化用的数据
    delete_data=member.load_yml("data/contact/member/member_para.yml")
    delete_data=delete_data["delete"]
    delete_ids=delete_data["ids"]
    delete_para=delete_data["data"]




    @pytest.mark.parametrize(("userid,name,mobile,department,errcode,errmsg"),
                             (["t","t","13172661165",[1,2],0,"abc"],
                             ["to","to","13172661165",[1,2],0,"abc"],
                             ["ton","ton","13172661165",[1,2],0,"abc"]),ids=ids)
    def test_add_member(self,access_token,userid,name,mobile,department,errcode,errmsg):
        # 1.获取access_token
        # 2.添加联系人
        res = self.member.add_member(access_token,userid,name,mobile,department)
        assert   errcode==res["errcode"]
        assert  errmsg in res["errmsg"]


    @pytest.mark.parametrize(("userid,errcode,errmsg"),delete_para,ids=delete_ids)
    def test_delete_member(self,access_token,userid,errcode,errmsg):
        # 1.获取access_token
        # 2.添加联系人
        res =self.member.delete_member(access_token,"abc")
        assert   errcode==res["errcode"]
        assert  errmsg in res["errmsg"]

