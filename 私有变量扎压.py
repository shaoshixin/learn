'''
    Python中将以两个或多个下划线字符开头并且没有两个或两个以上下划线结尾的变量当作私有
    变量。私有变量会在代码生成前被转换成长格式（变为公有）
    转换机制：在变量前端插入类名，再在前端加入一个下划线字符。这就是所谓的私有变量扎压
    注意：扎压会使标识符变长，超过255时就会被自动切断。当类名全部以下划线命名时不进行扎压
'''
class A(object):
    def __init__(self):
        self.__private()
        self.public()

    def __private(self):
        print('A.__private()')

    def public(self):
        print('A.public()')


class B(A):
    '''
    继承了A的__init__进行初始化，但是self.__private()被扎压成为self._A__private()，
    相应的下面的函数名也变成了 def _A__private()
    所以会输出A.__private()和B.public()
    '''
    def __private(self):
        print('B.__private()')

    def public(self):
        print('B.public()')


b = B()
