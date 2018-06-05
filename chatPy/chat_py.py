# -*- coding: utf-8 -*-
# @Project : upupup 
# @Time    : 2018/6/5 13:06
# @Author  : 
# @File    : chat_py.py
# @Software: PyCharm Community Edition

import itchat
import tkinter as tk
from PIL import Image
import os
import math
import threading
from tkinter import messagebox
class ChatPy():
    def __init__(self):
        self.img_path = 'imgs'
        self.root = tk.Tk()
        self.root.title(u'头像拼图')
        self.root.geometry('300x100')
        self.gui_grid()
        self.run_gui()

    def login_wechat(self):
        itchat.auto_login()
        self.user_name_value_lable.config(text=self.get_myself_info()['NickName'])
        self.login_button.config(text=u'请稍等...',state='disable')
        t1 = threading.Thread(target=self.get_head_image)
        t1.start()
        # self.get_head_image()
        # self.pingjie_img()
    def get_firends_list(self):
        return itchat.get_friends()
    def get_myself_info(self):
        return self.get_firends_list()[0]
    def get_all_firends_list(self):
        return self.get_firends_list()[1:]
    def get_head_image(self):
        if os.path.exists(self.img_path):
            for x in os.listdir(self.img_path):
                os.remove('{}/{}'.format(self.img_path,x))
        else:
            os.mkdir(self.img_path)
        n=1
        for fr in self.get_firends_list():
            # print(fr)
            r=itchat.get_head_img(fr["UserName"])
            with open('{}/{}.jpg'.format(self.img_path,n),'wb') as fp:
                fp.write(r)
                fp.close()
                n+=1
        self.pingjie_img()
    def pingjie_img(self):
        dirs=os.listdir(self.img_path)
        each_size = int(math.sqrt(float(800.0*800.0) / len(dirs)))
        print(each_size)
        line = int(800.0 / each_size)
        photographic = Image.new("RGB", (800, 800))
        x = 0
        y = 0
        for i in range(1, len(dirs)):
            try:
                imageOfFriends = Image.open("{}/{}.jpg" .format(self.img_path,i))  # 打开一张照片，PIL库的应用
            except IOError:
                print("error")
            else:
                image_resize = imageOfFriends.resize((each_size, each_size))
                photographic.paste(image_resize, (x * each_size, y * each_size))
                x += 1
                if x == line:
                    x = 0
                    y += 1
                    # 保存图像，发送给文件助手，显示图像
        photographic.save('logo.jpg')
        itchat.send_image('logo.jpg','filehelper')
        messagebox.showinfo('提示','图片已发送到【文件传输助手】！请查收确认')
        itchat.logout()
        self.login_button.config(text=u'生成拼图',state='normal')
    def gui_grid(self):
        login_frame=tk.LabelFrame(self.root,width=300, height=100, text='',relief='groove')
        user_name_lable = tk.Label(login_frame, text=u'头像越多时间越长!')
        self.user_name_value_lable=tk.Label(login_frame,text=u'点击\'生成拼图\',并扫描二维码')
        self.login_button=tk.Button(login_frame,text=u'生成拼图',command=self.login_wechat)
        #ui grid
        login_frame.grid(row=0, column=0)
        user_name_lable.place(x=0, y=0)
        self.user_name_value_lable.place(x=0, y=20)
        self.login_button.place(x=140,y=0,height=20)

    def run_gui(self):
        self.root.mainloop()

if __name__=="__main__":
    a=ChatPy()
