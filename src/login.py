import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
import os
from PIL import Image, ImageTk
from src.sql import db


class LoginWindow(Tk):
    """
    创建登录窗体的GUI界面已经登录的方法
    """

    LoginFlag = False
    user_name = ""

    def __init__(self):
        super().__init__()  # 先执行tk这个类的初始化
        self.title("登录界面")
        # self.geometry("620x420")
        self.resizable(False, False)  # 窗体大小不允许变，两个参数分别代表x轴和y轴
        # self.iconbitmap("." + os.sep + "img" + os.sep + "student.ico")
        # self["bg"] = "royalblue"
        # 加载窗体
        self._setup_ui()

    def _setup_ui(self):
        # ttk中控件使用style对象设定
        self.Style01 = Style()
        self.Style01.configure("user.TLabel", font=("华文黑体", 20, "bold"), foreground="royalblue")
        self.Style01.configure("TEntry", font=("华文黑体", 20, "bold"))
        self.Style01.configure("TButton", font=("华文黑体", 20, "bold"), foreground="royalblue")
        # 创建一个Label标签展示图片
        img = Image.open("." + os.sep + "src" + os.sep + "login-bcakground.png")
        self.Login_image = ImageTk.PhotoImage(img)
        self.Label_image = Label(self, image=self.Login_image)
        self.Label_image.pack(padx=10, pady=10)
        # 创建一个Label标签 + Entry   --- 用户名
        self.Label_user = Label(self, text="用户名:", style="user.TLabel")
        self.Label_user.pack(side=LEFT, padx=10, pady=10)
        self.Entry_user = Entry(self, width=12)
        self.Entry_user.pack(side=LEFT, padx=10, pady=10)
        # 创建一个Label标签 + Entry   --- 密码
        self.Label_password = Label(self, text="密码:", style="user.TLabel")
        self.Label_password.pack(side=LEFT, padx=10, pady=10)
        self.Entry_password = Entry(self, width=12, show="*")
        self.Entry_password.pack(side=LEFT, padx=10, pady=10)
        # 创建一个按钮    --- 登录
        self.Button_login = Button(self, text="登录", width=4, command=self._login)
        self.Button_login.pack(side=LEFT, padx=20, pady=10)

    def _login(self):
        user = self.Entry_user.get()
        password = self.Entry_password.get()
        flag = db.login(user, password)
        if flag:
            tkinter.messagebox.showinfo(title="Success", message="登录成功！！")
            self.LoginFlag = True
            self.user_name = user
            self.destroy()
            # main_window = MainWindow()
        else:
            self.LoginFlag = False
            tkinter.messagebox.showerror(title="Fail", message="登录失败，请检查用户名与密码")


if __name__ == '__main__':
    this_login = LoginWindow()
    this_login.mainloop()
