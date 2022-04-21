# -*- coding: utf-8 -*-
# author：slz time:2022/4/20
'''
'''
import re


class TestData:
    id = 10
    name = 'slz'
    data = '0011'
    title = 'OK'


params = "{'id': '#id#', 'name': '#name#', 'data': '#data#', 'title': '#title#'}"



while re.search('#(.+?)#', params):
    res = re.search('#(.+?)#', params)
    item = res.group()
    attr = res.group(1)
    value = getattr(TestData, attr)
    params = params.replace(item, str(value))

    print(params)


# params = params.replace('#id#', str(id))
# params = params.replace('#name#', str(name))
# params = params.replace('#data#', str(data))
# params = params.replace('#title#', str(title))