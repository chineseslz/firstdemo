# -*- coding: utf-8 -*-
# author：slz time:2022/4/15
'''
'''
import pymysql
from firstdemo.jieKouDemo.shiZhanDemo.common.handle_conf import conf


class HandleDB:
    def __init__(self, *args, **kwargs):
        self.con = pymysql.Connect(host=conf.get('mysql', 'host'),
                                   port=conf.getint('mysql', 'port'),
                                   user=conf.get('mysql', 'user'),
                                   password=conf.get('mysql', 'password'),
                                   charset=conf.get('mysql', 'charset'),
                                   cursorclass=pymysql.cursors.DictCursor,
                                   *args, **kwargs
                                   )

    def find_one(self, sql):
        with self.con as cur:
            cur.execute(sql)
        cur.close()
        return cur.fetchone()

    def find_all(self, sql):
        with self.con as cur:
            cur.execute(sql)
        cur.close()
        return cur.fetchall()

    def find_count(self, sql):
        with self.con as cur:
            res = cur.execute(sql)
        cur.close()
        return res

    def __del__(self):
        self.con.close()


if __name__ == '__main__':
    sql = 'select * from futureloan.member LIMIT 5 '
    db = HandleDB()
    res = db.find_all(sql)
    print(res)
