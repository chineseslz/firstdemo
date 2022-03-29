# -*- coding: utf-8 -*-
# author：slz time:2022/3/29
'''
'''
import requests

url1 = "http://api.lemonban.com/futureloan/member/login"
params1 = {
    "mobile_phone": "13921840178",
    "pwd": "lemonban"
}
header1 = {
    "X-Lemonban-Media-Type": "lemonban.v2"
}
response = requests.post(url=url1, headers=header1, json=params1)
res = response.json()
# 从字典获取token和id
token = res['data']['token_info']['token']
mem_id = res['data']['id']

url2 = "http://api.lemonban.com/futureloan/member/recharge"
params2 = {
    "member_id": mem_id,
    "amount": 3000
}
# 请求头
header2 = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "Authorization": "Bearer " + token
}
requests.post(url=url2,json=params2,headers=header2)
print(response.json())