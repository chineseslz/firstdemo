# -*- coding: utf-8 -*-
# author：slz time:2022/3/30
'''
jsonpath方法需要两个参数：
参数1：数据
参数2：jsonpath表达式

jsonpath表达式语法：
$       --->        根节点
.       --->        选择直接子节点
..      --->        选择子孙节点（不管层级）
[]      --->        选择子节点/选择索引
[,]     --->        选择多个字段
@       --->        代表当前选中节点（通常和条件过滤一起使用）
[?(过滤条件)]        通过条件过滤选择数据


1.如果没有匹配到数据返回的是false
2.如果匹配到数据返回的是包含数据的列表

'''
from jsonpath import jsonpath

# import requests
# response = requests.get("https://www.xfz.cn/api/website/partners/")
# print(response.json())

data = {
    'code': 200,
    'data': [
        {'photo': 'https://static-image.xfz.cn/1454046552_487.png',
         'create_time': '2016-01-29 13:49:13',
         'link': 'http://www.ehoutai.com/',
         'uid': 7, 'name': '易后台'},
        {'photo': 'https://static-image.xfz.cn/1454046135_474.png',
         'create_time': '2016-01-29 13:42:15',
         'link': 'http://www.sanjieke.com/',
         'uid': 4, 'name': '三节课'},
        {'photo': 'https://static-image.xfz.cn/1454046053_122.png',
         'create_time': '2016-01-29 13:40:53',
         'link': 'https://www.aliyun.com/',
         'uid': 1, 'name': '阿里云'},
        {'photo': 'https://static-image.xfz.cn/1454047318_361.png',
         'create_time': '2016-01-29 14:01:59',
         'link': 'http://xmanlegal.com/',
         'uid': 8, 'name': '未来法律'}]
}

data2 = {
    "code": 0,
    "msg": "ok",
    "data": {
        "id": 34300683,
        "leave_amount": 10000.0,
        "mobile_phone": "13921840178",
        "reg_name": "小柠檬",
        "reg_time": "2022-03-25 13:49:52.0",
        "type": 1,
        "token_info": {
            "token_type": "Bearer",
            "expires_in": "2022-03-30 14:35:36",
            "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjM0MzAwNjgzLCJleHAiOjE2NDg2MjIxMzZ9.KdQl41YbdkkRv7gEQ8IIipwXRPpCf8EBOvT4Q10beSEYGPpOaxEzQE3cbIUzcOuDIsgYzKgRIqqPUxzXc-fc8g"
        }
    },
    "copyright": "Copyright 柠檬班 © 2017-2019 湖南省零檬信息技术有限公司 All Rights Reserved"
}

# token = jsonpath(data2,"$..token")
# token = jsonpath(data, "$.data[0]")
# token = jsonpath(data,"$.data[0][uid,name]")
token = jsonpath(data,"$.data[?(@.uid==4)].name")

print(token)


