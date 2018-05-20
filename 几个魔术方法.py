#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 11:04
# @Author  : Shao
# @File    : 几个魔术方法.py
# @Desc    :python的魔术方法，生命周期
#           每一个(大部分)内建函数（BIF）后都有一个对应的魔术方法
#           __new__：用来实例化类，返回一个类的对象，很少会用到。
#           __init__初始化实例的值，经常用到。二者相当于“构造函数”
#           __del__“构析函数”，当对象生命周期结束时调用,不常用
#           __str__转换为字符串，__repr__转换为机器能识别的字符串，也就是转换后的字符串能直接执行__unicode__转换成字符串

class P:
    # def __new__(cls, *args, **kwargs):
    #     pass

    def __init__(self, name,age):
        self.name = name
        self.age = age
        # return "s"  # 这样是错误的，__init__方法不能返回除None外的任何值
        #print(self.name + self.age) 这样是正确的

    def __str__(self):#覆写__str__魔术方法，即改变了str方法，在print方法使用时先调用str方法转换成字符串，变相的改变了输出
        return '这是覆写str的P  ' + self.name

    # def __del__(self):
    #     self.file.close()
    #     del self.file


class Q(P):
    def __init__(self,name,age,wigth):
        '''
         若子类没有定义自己的初始化函数，会自动继承父类的初始化函数
         若子类定义了自己的初始化函数，且没有显示的调用父类初始化函数，则初始化函数被覆写，父类初始化函数不会被调用
         显示的调用父类的初始化函数，以添加子类独有的方法属性
        '''
        super(Q,self).__init__(name,age)
        self.wigth = wigth

    def __str__(self):#这又覆盖了父类的str，否则会输出父类的__str__
        return '这是覆写str的Q  ' + self.name + self.age +self.wigth

if __name__ == '__main__':
    q = Q('wang','1','12')
    p = P('ming','12')
    print(q)#由于覆写了__str__魔术方法，此时q = q.name + q.age +q.wigth
    print("这是正常打印的Q  " + q.name + q.age + q.wigth)
    print(p)
