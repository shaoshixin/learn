#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 16:44
# @Author  : Shao
# @File    : main.py
# @Desc    :


from tkinter import *
import Model as ma





class MainPage:
    def __init__(self, master=None):
        self.root = master
        self.creatPage()

    def __quit(self):
        self.root.quit()
        root.destroy()
        exit()

    def creatPage(self):

        m = ma(self.root)

        lab = Label(self.root, text='测试')
        lab.pack();
        menuBar = Menu(self.root)
        fileMenu = Menu(menuBar, tearoff=False)
        fileMenu.add_command(label='账户密码组合生成！', command=go)
        menuBar.add_cascade(label='数据生成', menu=fileMenu)
        menuBar.add_separator()
        urlMenu = Menu(menuBar, tearoff=False)
        urlMenu.add_command(label='占位', command=m())
        urlMenu.add_command(label='占位', command=go)
        menuBar.add_cascade(label='url输入', menu=urlMenu)
        menuBar.add_separator()
        menuBar.add_command(label='退出', command=self.__quit)
        root.config(menu=menuBar)


def go():
    print("go")


if __name__ == '__main__':
    root = Tk()
    root.title('nihao')
    main_page = MainPage(root)
    width = 600
    height = 600
    root.geometry(
        '%dx%d+%d+%d' % (width, height, (root.winfo_screenwidth() - width) / 2,
                         (root.winfo_screenheight() - height) / 2))
    root.mainloop()
