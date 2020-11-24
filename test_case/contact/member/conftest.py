import pytest

from api.contact.member import Member

member=Member()
# 增加联系人的前后置步骤
@pytest.fixture(scope="session")
def add(access_token):
    # 想要删除联系人
    member.delete_member(access_token,"tongtongtong1234")
    # 添加后置,yield作为后置的关键字
    yield
    member.delete_member(access_token, "tongtongtong1234")

# 删除联系人前后置的步骤
@pytest.fixture(scope="session")
def delete(access_token):
    # 添加联系人，方便删除联系人执行成功
    member.add_member(access_token,"tongtongtong1234","tongtongtong1234","13172667777",[1,2])