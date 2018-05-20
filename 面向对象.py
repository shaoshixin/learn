#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 11:04
# @Author  : Shao
# @File    : 面向对象.py
# @Desc    :python的魔术方法，生命周期
#           __new__：用来实例化类，返回一个类的对象，很少会用到。
#           __init__初始化实例的值，经常用到。二者相当于“构造函数”
#           __del__“构析函数”，当对象生命周期结束时调用,不常用
from os.path import join


class P:
    def __new__(cls, *args, **kwargs):
        pass

    def __init__(self, filepath='~', filename='test.txt'):
        self.file = open(join(filepath, filename), 'r+')
        return "s"  # 这样是错误的，__init__方法不能返回除None外的任何值

    def __del__(self):
        self.file.close()
        del self.file


if __name__ == '__main__':
    file = P
    print(file.__dict__)
