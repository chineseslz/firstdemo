'''
    读取文件  日期处理  公共
'''
from datetime import datetime, date, timedelta

import xlrd


def date_n(n):
    return str(date.today() + timedelta(days=int(n)))


# ishead  是否需要有标题    有就是true  没有就是false  默认false
def read_excel(filename, index, ishead=False):
    xlsx = xlrd.open_workbook(filename)
    sheet = xlsx.sheet_by_index(index)
    data = []
    for i in range(sheet.nrows):
        if i == 0:
            if ishead:
                continue
        data.append(sheet.row_values(i))
    return data
