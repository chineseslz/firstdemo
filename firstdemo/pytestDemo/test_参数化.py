import pytest
import requests

# @pytest.mark.parametrize('a,b,c',[(1,2,3),(0,1,1),(1,-1,0)])
# def test(a,b,c):
#     print(a+b==c)

cases = [('成功登陆','admin', '123456', '0000', 'login-pass'),
        ('用户名错误','admin1', '123456', '0000', 'login-fail'),
        ('密码错误','admin', '123', '0000', 'login-fail'),
        ('密码为空','admin', '', '0000', 'login-fail'),
        ('验证码错误','admin', '', '123456', 'vcode-error'), ]

@pytest.mark.parametrize("name,user,pwd,vcode,ex",cases)
def test_login(name,user,pwd,vcode,ex):
    url = ''
    rq = requests.session()
    login_data = {'username':user,'password':pwd,'verifycode':vcode}
    r = rq.post(url=url,data = login_data)
    assert r.text == ex

if __name__ == '__main__':
    pytest.mark(['-s', __file__])
