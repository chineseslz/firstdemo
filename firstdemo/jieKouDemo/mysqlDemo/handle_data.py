# -*- coding: utf-8 -*-
# author：slz time:2022/4/21
'''
'''
import re
from jieKouDemo.shiZhanDemo.common.handle_conf import conf


class TestData:
    id = 10
    name = 'slz'
    data = '0011'
    title = 'OK'


params = "{'id': '#id#', 'name': '#name#', 'data': '#data#', 'title': '#title#'}"


# --------------------------升级版本，初版在下面注释了----------------
def replace_data(data, cls):
    '''
    :param data: 要进行替换的用例数据
    :param cls: 测试类
    :return:
    '''
    while re.search('#(.+?)#', data):
        res = re.search('#(.+?)#', data)
        item = res.group()
        attr = res.group(1)
        try:
            value = getattr(cls, attr)
        except AttributeError:
            value = conf.get('test_data', attr)
        data = data.replace(item, str(value))
    return data


if __name__ == '__main__':
    data = replace_data(params, TestData)
    print(data)

'''
def replace_data(data, cls):
  
  :param data: 要进行替换的用例数据
  :param cls: 测试类
  :return:
  
  while re.search('#(.+?)#', data):
      res = re.search('#(.+?)#', data)
      item = res.group()
      attr = res.group(1)
      value = getattr(cls, attr)
      data = data.replace(item, str(value))
  return data
'''
