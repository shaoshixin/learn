#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 9:16
# @Author  : Shao
# @File    : main.py
# @Desc    :通过字典实现switch操作，很棒

from __future__ import division
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y

operator = {"+": add, "-": sub, "*": mul, "/": div}
operator["+"](1, 2) # the same as add(1, 2)
operator["/"](1, 2) # error, not have key "%", but the below will not
'''
    dict.get(key,default=None)
    字典的get()方法，查找键为key的值，若不存在返回后面的默认值
'''
operator.get("+")(1, 2) # the same as add(1, 2)

def cal(x, o, y):
    print(operator.get(o)(x, y))
cal(2, "/", 3)
	# this method will effect than if-else


if __name__ == '__main__':
    pass