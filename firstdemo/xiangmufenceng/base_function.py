'''
    基础层代码
    准备环境
'''
from datetime import datetime, date, timedelta

import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By


def date_n(n):
    return str(date.today() + timedelta(days=int(n)))



def get_driver():
    return webdriver.Chrome()


driver = get_driver()

def byname(element):
    return driver.find_element(By.NAME, element)


def byxpath(element):
    return driver.find_element(By.XPATH, element)


def open_url(url):
    driver.get(url)
    driver.maximize_window()


def close():
    driver.quit()


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