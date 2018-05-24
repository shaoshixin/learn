from tkinter import *
from tkinter.messagebox import *


class Model:
    def __init__(self, master=None):
        self.root = master
        self.username = StringVar()
        self.password = StringVar()
        self.creatPage()

    def creatPage(self):
        self.frame = Frame(self.root)
        self.frame.pack()
        # self.frame = Frame(self.root)  # 创建Frame
        Label(self.frame).grid(row=0, stick=W)
        Label(self.frame, text='账户: ').grid(row=1, stick=W, pady=10)
        Entry(self.frame, textvariable=self.username).grid(row=1, column=1,
                                                           stick=E)
        Label(self.frame, text='密码: ').grid(row=2, stick=W, pady=10)
        Entry(self.frame, textvariable=self.password, show='*').grid(row=2,
                                                                     column=1,
                                                                     stick=E)
        Button(self.frame, text='登陆', command=self.loginCheck).grid(row=3,
                                                                    stick=W,
                                                                    pady=10)
        Button(self.frame, text='退出', command=self.frame.quit).grid(row=3,
                                                                    column=1,
                                                                    stick=E)

    def loginCheck(self):
        name = self.username.get()
        secret = self.password.get()
        if name == '1' and secret == '1':
            self.frame.destroy()
            showinfo(title='成功', message='cheng')
        else:
            showinfo(title='错误', message='账号或密码错误！')
