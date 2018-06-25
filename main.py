#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 16:44
# @Author  : Shao
# @File    : main.py
# @Desc    :


from tkinter import *
from Model import *
from frame import *
from f1 import *


class MainPage:
    def __init__(self, master=None):
        self.root = master
        # self.main_menu_frm = Frame(self.root)
        self.model_frm = Model(self.root)
        self.model_frm.pack()
        self.help_frm = Fr(self.root)
        self.creatMenu()

    def __quit(self):
        self.root.quit()
        root.destroy()
        exit()

    def creatMenu(self):

        lab = Label(self.root, text='测试')
        lab.pack();
        # self.main_menu_frm.pack()

        menuBar = Menu(self.root)
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label='账户密码组合生成！', command=self.go)
        menuBar.add_cascade(label='数据生成', menu=fileMenu)
        menuBar.add_separator()
        urlMenu = Menu(menuBar, tearoff=False)
        urlMenu.add_command(label='占位1', command=self.go)
        urlMenu.add_command(label='占位2', command=self.go1)
        urlMenu.add_command(label='占位3', command=self.go2)
        menuBar.add_cascade(label='url输入', menu=urlMenu)
        menuBar.add_separator()
        menuBar.add_radiobutton(label='退出', command=self.__quit)
        root.config(menu=menuBar)

    def go(self):
        self.model_frm.forget()
        self.help_frm.forget()

    def go1(self):
        self.model_frm.forget()
        self.help_frm.pack()

    def go2(self):
        self.model_frm.pack()
        self.help_frm.forget()



if __name__ == '__main__':
    root = Tk()
    root.title('nihao')
    MainPage(root)
    width = 600
    height = 600
    root.geometry(
        '%dx%d+%d+%d' % (width, height, (root.winfo_screenwidth() - width) / 2,
                         (root.winfo_screenheight() - height) / 2))
    root.mainloop()
