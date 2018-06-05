# -*- coding: utf-8 -*-
# @Project : upupup 
# @Time    : 2018/6/5 13:06
# @Author  : 
# @File    : chat_py.py
# @Software: PyCharm Community Edition

import itchat
import tkinter as tk

class ChatPy():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('chatPy')
        self.root.geometry('710x600')
        self.login_wechat()
        self.gui_grid()
        self.run_gui()
    def login_wechat(self):
        itchat.auto_login(hotReload=True)
    def get_firends_list(self):
        return itchat.get_friends()
    def get_myself_info(self):
        return self.get_firends_list()[0]
    def get_all_firends_list(self):
        return self.get_firends_list()[1:]

    def gui_grid(self):
        login_frame=tk.LabelFrame(self.root,width=300, height=100, text='登录',relief='groove')
        user_name_lable = tk.Label(login_frame, text='user:')
        user_name_value_lable=tk.Label(login_frame)
        #ui grid
        login_frame.grid(row=0, column=0)
        user_name_lable.place(x=0, y=0)
        user_name_value_lable.place(x=80, y=0)
        user_name_value_lable.config(text=self.get_myself_info()['NickName'])
    def run_gui(self):
        self.root.mainloop()

if __name__=="__main__":
    a=ChatPy()
