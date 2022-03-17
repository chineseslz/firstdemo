'''
    测试层代码
'''

from quna_book import *

def test_book_ticket():
    start = "南京"
    end = "青岛"
    n = 2
    name = "孙梁柱"
    id = "320902199608236306"
    book_ticket(start,end,n,name,id)

if __name__ == '__main__':
    test_book_ticket()