# -*- coding: utf-8 -*-
# author：slz time:2022/3/29
'''
'''
import requests

#创建一个会话对象  （使用这个session对象去发送请求，会自动化记录请求的cookie信息，下一次请求会自动化添加cookie）
s = requests.session()

url = "https://openapiv5.ketangpai.com//UserApi/login"
params = {
    "email":"88058173@qq.com",
    "password":"sun1996823",
    "remember":0
}
response = s.post(url=url,data=params)
print(response.json())

url = "https://openapiv5.ketangpai.com//UserApi/getUserVipSetting"
response = s.get(url=url)
print(response.json())