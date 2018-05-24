#!/usr/bin/env python
# @Time    : 2018/5/24 10:59
# @Author  : Shao
# @File    : 造假数据.py.py
# @Desc    :


import json
from faker import Faker

# fake = Faker('en_US')
fake = Faker('zh_CN')
person_dict = {}
p = {}
person_list = []
for i in range(0, 100):
    person_list.append(fake.address())
    # person_list.append(fake.phone_number())
    person_dict["姓名测试"] = person_list
with open("D:/projects/python36/learn/1.json", "w", encoding="utf-8") as f:
    # 如果字符串是这样定义：s=u'中文'
    # 则该字符串的编码就被指定为unicode了，即python的内部编码，而与代码文件本身的编码无关。
    # 因此，对于这种情况做编码转换，只需要直接使用encode方法将其转换成指定编码即可。
    # 存在于list,dict等容器中的unicode字符就是一这种编码方式存在的，单独打印某一项的时候，
    # 会显示成中文字符，但是直接打印整个list的时候，就不会做字符映射以正确显示中文
    # ensure_ascii=False 不以unicode编码
    f.write(json.dumps(person_dict, ensure_ascii=False))
print(person_dict)
