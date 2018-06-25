from tkinter import *
from tkinter.messagebox import *


class Model(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.username = StringVar()
        self.password = StringVar()
        self.creatPage()

    def creatPage(self):
        Label(self, text='账户: ').pack()
        Entry(self, textvariable=self.username).pack()
        Label(self, text='密码: ').pack()
        Entry(self, textvariable=self.password, show='*').pack()
        Button(self, text='登陆', command=self.loginCheck).pack()
        Button(self, text='退出', command=self.root.quit).pack()

    def loginCheck(self):
        name = self.username.get()
        secret = self.password.get()
        if name == '1' and secret == '1':
            self.root.destroy()
            showinfo(title='成功', message='cheng')
        else:
            showinfo(title='错误', message='账号或密码错误！')


if __name__ == '__main__':
    root = Tk()
    root.title('nihao')
    main_page = Model(root)
    width = 600
    height = 600
    root.geometry(
        '%dx%d+%d+%d' % (width, height, (root.winfo_screenwidth() - width) / 2,
                         (root.winfo_screenheight() - height) / 2))
    root.mainloop()
