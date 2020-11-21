from api.get_token import GetToken
from common.get_config import cf
import pytest

@pytest.fixture(scope="session")
def access_token():
    secret=cf.get_value("wework","contact_secret")
    token=GetToken().get_token(secret)
    return token