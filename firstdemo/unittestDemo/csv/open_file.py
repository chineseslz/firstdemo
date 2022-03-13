# #txt获取
# f = open('aaa.txt','r',encoding='utf-8')
# print(f.read())
#
# #csv获取
# import csv
# f= open('aaa.csv','r',encoding='utf-8')
# c = csv.reader(f)
# for cs in c:
#     print(cs)

#xlsx获取
import xlrd
lsx = xlrd.open_workbook("aaa.xlsx")
sheet = lsx.sheet_by_index(0)
# print(sheet.nrows)  #行
# print(sheet.ncols)  #列
# print(sheet.row_values(0))
for i in range(sheet.nrows):
    print(sheet.row_values(i))

# #json获取
# json_str = open("aaa.json","r",encoding="utf-8").read()
# print(json_str)
#
# import json
# j = json.loads(json_str)   #文本转换到json
# print(j)
# print(j[0]["name"])
#
# print(json.dumps(j,ensure_ascii=False))  #json转换到文本


# #xml获取
# try:
#     import xml.etree.cElementTree as ET
# except ImportError:
#     import xml.etree.cElementTree as ET
#
# tree = ET.parse("aaa.xml")
# root = tree.getroot()
# # print(root.tag)
# # print(root.attrib)
# # print(root.text)
#
# for child in root:
#     # print(child.tag)
#     # print(child.attrib)
#     # print(child.text)
#     print("------------")
#     for children in child:
#         print(children.tag)
#         print(children.attrib)
#         print(children.text)

# #yaml获取
# import yaml
# yaml_str = open("aaa.yaml","r",encoding="utf-8").read()
#
# yaml_ob = yaml.load(yaml_str,Loader=yaml.FullLoader)
# print(yaml_ob)