#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 22:43
# @Author  : Shao
# @Site    :
# @Notes   :单下划线开头的属性方法

class oldC():
    c = "s"  # 注意在__init__初始化方法中初始化属性和在此处初始化的区别，此处初始化的属性所有该类的实例均共享，修改后全部
    # 被修改
    def __init__(self, a, b):
        self.name = a
        self.age = b

    def getOld(self):
        print("xing" + self.name)


class newC(object):
    def __init__(self, a, b):
        self.name = a
        self.age = b

    def getNew(self):
        print("姓名是：" + self.name)

    def __getA(self):
        print("newC__get")


if __name__ == '__main__':
    old = oldC("ming", 10)
    print(old.__dict__)
    new = newC("wa", 11)
    print(new._newC__getA())  # 访问双下划綫开头的私有方法
    print(type(old))  # type打印其类型
    print(dir(new))  # dir打印
    print(type(new))  # python3中不存在新式类和老实类的区别
