'''
    测试层代码
    测试数据
'''

from quna_book import *
from base_function import *

date = read_excel("aaa.txt", 0, True)


#   @pytest.mark.parametrize(["start","end","n","name","id"],data)
def test_book_ticket(start, end, n, name, id):
    book_ticket(start, end, n, name, id)


if __name__ == '__main__':
    test_book_ticket()
