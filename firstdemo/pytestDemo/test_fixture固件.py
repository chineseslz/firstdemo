'''
name：指定fixture名称，如果不指定则默认为被装饰的函数名
scope：指定fixture作用范围，默认模块级别。module，function，class，session，package
params：参数
autouse：设置为True：实现自动调用fixture
'''

import pytest
import requests

# #局部

# #创建fixture
# @pytest.fixture(scope='module')
# def login():
#     print('登录')
#     yield '注销'    #通过yield 实现后置
#
# def test_add(login):
#     print('添加会员')
#
# def test_query_store(login):
#     print('库存查询')
#
# if __name__ == '__main__':
#     pytest.main(['-s',__file__])


@pytest.fixture(name='fx',autouse=True,scope='module')
def login_logout():
    rq = requests.session()
    url = 'http://192.168.0.200:8080/#/login'
    login_data = {'username':'admin','passowrd':'admin'}
    rq.post(url=url,data=login_data)
    print('登录成功')
    yield rq
    url = 'http://192.168.0.200:8080/#/logout'
    rq.get(url=url)
    print("注销成功")







