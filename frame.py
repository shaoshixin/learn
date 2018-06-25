import tkinter as tk
import f1


class mainPage:
    def __init__(self, master=None):
        self.root = master
        self.main_menu = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.main_menu, tearoff=0)
        self.help_menu = tk.Menu(self.main_menu, tearoff=0)
        self.creatmenu()

    def creatmenu(self):
        self.file_menu.add_command(label='open', command=self.go)
        self.file_menu.add_command(label='save', command=self.go)
        self.main_menu.add_cascade(label='file_menu', menu=self.file_menu)
        tk.Label(self.root, text='账户: ').pack()

        root.config(menu=self.main_menu)

    def go(self):
        print('go')


if __name__ == '__main__':
    root = tk.Tk()
    root.title = 'main'
    width = 600
    height = 600
    root.geometry(
        '%dx%d+%d+%d' % (width, height, (root.winfo_screenwidth() - width) / 2,
                         (root.winfo_screenheight() - height) / 2))
    mainPage(root)
    root.mainloop()
