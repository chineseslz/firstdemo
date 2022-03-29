# -*- coding: utf-8 -*-
# author：slz time:2022/3/29
'''
'''
import requests

# ---------------------------------------参数类型：json--------------------------------
# url = "http://api.lemonban.com/futureloan/member/register"
# #请求头
# head = {
#     "X-Lemonban-Media-Type":"lemonban.v1"
# }
# #参数
# params = {
#     "mobile_phone":"13921840178",
#     "pwd":"lemonban"
# }
#
# #参数类型 是json情况下，需要json来传递参数
# response = requests.post(url=url,headers=head,json=params)
# print(response.text)

# ---------------------------------------get 请求的参数--------------------------------
# 方式一：参数直接拼接在url上
# url = "http://api.lemonban.com/futureloan/loans?pageIndex=1&pageSize=20"
# head = {
#     "X-Lemonban-Media-Type": "lemonban.v1"
# }
# response = requests.get(url=url,headers=head)
# 方式二：使用params拼接
# url = "http://api.lemonban.com/futureloan/loans"
# params = {
#     "pageIndex":1,
#     "pageSize":20
# }
# response = requests.get(url=url,headers=head,params=params)
# print(response.text)


# ---------------------------------------form-data--文件上传------------------------------
# 除了上传的文件，接口其他参数不能放入files中
url = ""
head = {

}
files = {
    "pic":("xx.gif",open("xx.gif","rb"),"images/git")
}
#其他参数
data = {
    "nickname":"slz",
    "age":18,
    "sex":"男"
}
response = requests.post(url=url,headers=head,files=files,data=data)