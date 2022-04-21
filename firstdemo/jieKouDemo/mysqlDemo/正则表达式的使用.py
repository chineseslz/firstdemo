# -*- coding: utf-8 -*-
# author：slz time:2022/4/20
'''
'''
import re
'''单字符
\d  表示数字
\D  表示非数字
\s  表示空白
\S  表示非空白
\w  表示单词字符
\W  表示非单词字符
.   表示任意字符
[]  例举匹配的单字符   [0-9a-zA-Z]
                    中文字符正则表达式：[\u4e00-\u9f5a]
'''

str1 = "asdasdsadas139218_40178sdadasd1孙梁柱7551052366as"
res1 = re.findall("[\u4e00-\u9f5a]",str1)
print(res1)


'''数量
*       匹配前一个字符出现0次以上           贪婪模式
+       匹配前一个字符出现1次以上           等同于==>{1,}
?       匹配前一个字符出现1次或者0次        懒惰模式
{m}     匹配前一个字符出现m次
{m,}    匹配前一个字符至少出现m次
{m,n}   匹配前一个字符出现m到n次
'''
params = '{"id": "#id#", "name": "#name#", "data": "#data#", "title": "#title#", "aaa": 111, "bbb": 222}'
res2 = re.findall("#.{1,}?#",params)
print(res2)


'''边界
^   表示字符串的开头
$   表示字符串的结尾
r\b  表示单词边界 (有空格或者标点符号)
\B  表示非单词边界
'''
s = '0123python465java'
res3 = re.findall('\B123',s)
print(res3)

'''分组
()  分组提取括号中的内容
|   表示多个匹配规则
'''
params1 = '{"id": "#id#", "name": "#name#", "data": "#data#", "title": "#title#", "aaa": 111, "bbb": 222}'
res4 = re.findall("#(.+?)#",params1)
print(res4)

s2 = '123456python345java0000'
res5 = re.findall('python|java',s)
print(res5)


'''
findall:匹配字符串中所有符合规则的数据并以列表的形式返回
search：匹配并返回第一个符合规则的匹配对象       .group()     .group(1)         没有匹配到返回none
'''
res6 = re.search("#(.+?)#",params1)
print(res6.group(1))








