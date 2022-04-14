# -*- coding: utf-8 -*-
# author：slz time:2022/4/14
'''
'''
import pymysql

# 1.连接数据库
con = pymysql.connect(
    host='api.lemonban.com',
    port=3306,
    user='future',
    password='123456',
    charset='utf8'
)

# #2.创建游标对象
cur = con.cursor()

sql = 'select leave_amount from futureloan.member where mobile_phone = "13265895752"; '
#3.执行sql
res = cur.execute(sql)
con.commit()
print(res)

#关闭
cur.close()
con.close()



# 创建一个游标对象（自动提交事务）
# with con as cur:
#     sql = 'select leave_amount from futureloan.member where mobile_phone = "13265895752"; '
#     res = cur.execute(sql)
#
# print(res)
#
# # 关闭
# cur.close()
# con.close()

'''
with 启动对象 上下文管理器 的关键字
上下文管理器协议：如果一个类中定义了如下两个方法 那么该类就实现了上下文管理器协议（可以通过with去进行操作）
__enter__:  'with XXX as' 后面的变量接收的是该方法的返回值
__exit__:   with中的 代码执行完毕之后会执行该方法
'''
