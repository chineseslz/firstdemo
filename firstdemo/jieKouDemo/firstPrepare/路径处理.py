import os

p1 = os.path.abspath("code.txt")   #绝对路径
p1 = os.path.abspath("..")   # 根路径
p1 = os.path.dirname(p1)  #获取所在目录的路径 （上级目录绝对路径）
print(p1)

#获取项目的跟目录路径
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#获取永猎数据文件夹所在的文件目录
data_dir = os.path.join(base_path,"pytestDemo")
