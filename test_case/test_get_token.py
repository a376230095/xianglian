from api.get_token import GetToken

class TestGetToken():
    a=GetToken()

    def test_get_token(self):
        token= self.a.get_token(self.a.secret)
        assert 214 ==len(token)