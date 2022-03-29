# -*- coding: utf-8 -*-
# author：slz time:2022/3/28
'''
'''
import requests

url = "http://www.lemonban.com/"
response = requests.get(url=url)

#-------------------------------响应的信息获取------------------------
#获取返回的相应状态码
# print(response.status_code)
#获取响应头
# print(response.headers)


#获取响应体
#方式一：自动识别返回内容的编码进行解码，(对返回任意类型的数据都可以使用)
# print(response.text)
#方式二：指定编码对返回内容进行解码
# print(response.content.decode('utf-8'))
#方式三：只能在返回数据是json的情况下使用（接口测试常用）
# print(response.json())


#-------------------------------请求的信息获取------------------------
#获取请求头
# print(response.request.headers)
#获取请求体
# print(response.request.body)








