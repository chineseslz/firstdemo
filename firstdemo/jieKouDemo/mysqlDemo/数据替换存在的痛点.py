# -*- coding: utf-8 -*-
# author：slz time:2022/4/20
'''
'''


class Test01:

    id = 10
    name = 'slz'
    data = "0011"
    title = "OK"


    params = '{"id": "#id#", "name": "#name#", "data": "#data#", "title": "#title#", "aaa": 111, "bbb": 222}'

    params = params.replace("#id#", str(id))
    params = params.replace("#name#", str(name))
    params = params.replace("#data#", str(data))
    params = params.replace("#title#", str(title))

    print(params)
