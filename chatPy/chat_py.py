# -*- coding: utf-8 -*-
# @Project : upupup 
# @Time    : 2018/6/5 13:06
# @Author  : 
# @File    : chat_py.py
# @Software: PyCharm Community Edition

import itchat
import tkinter as tk
from PIL import Image,ImageTk
import os
import math
import threading
from tkinter import messagebox
class ChatPy():
    def __init__(self):
        self.img_path = 'imgs'
        self.res_path='resources'
        self.current_user_logo_name= 'user_logo.jpg'
        self.default_user_log='moren.jpg'
        self.bg_image_name='bg.png'
        self.root = tk.Tk()
        self.root.title(u'头像拼图')
        self.root.geometry('300x100')
        self.gui_grid()
        self.run_gui()

    def login_web(self):
        itchat.auto_login()
        self.user_name_value_lable.config(
            text=self.get_myself_info()['NickName'],
            fg='blue',
            font=('黑体',12)
        )
        self.get_self_head_img()
        self.user_logo = self.get_head_img_50x50(self.img_path, self.current_user_logo_name)
        self.head_image_lable.config(image=self.user_logo)
        self.mix_logo_button.config(state='normal')
        self.login_button.config(state='disable',text='已登录')
        self.login_out_button.config(state='normal')
    def login_out(self):
        itchat.logout()
        self.user_name_value_lable.config(text=u'登录后点击\'生成拼图\',并扫描二维码')
        self.login_button.config(state='normal', text='登录')
    def mix_logo(self):
        self.mix_logo_button.config(text=u'请稍等...', state='disable')
        t1 = threading.Thread(target=self.get_head_image)
        t1.start()
    def get_firends_list(self)->list:
        return itchat.get_friends()
    def get_myself_info(self)->list:
        return self.get_firends_list()[0]
    def get_all_firends_list(self)->list:
        return self.get_firends_list()[1:]
    def get_head_img_50x50(self,res_path,image_name)->ImageTk.PhotoImage:
        head_img_pil=Image.open('{}/{}'.format(res_path,image_name))
        return ImageTk.PhotoImage(head_img_pil.resize((50,50)))
    def get_res_image(self,res_path,image_name,im_size_x,im_size_y)->ImageTk.PhotoImage:
        head_img_pil = Image.open('{}/{}'.format(res_path, image_name))
        return ImageTk.PhotoImage(head_img_pil.resize((im_size_x, im_size_y)))
    def get_self_head_img(self) ->None:
        im=itchat.get_head_img(self.get_myself_info()["UserName"])
        with open('{}/{}'.format(self.img_path, self.current_user_logo_name), 'wb') as fp:
            fp.write(im)
            fp.close()
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
        self.mix_logo_button.config(text=u'生成拼图', state='normal')
    def gui_grid(self):
        self.lab_bg = self.get_res_image(self.res_path, self.bg_image_name, 300, 100)
        login_frame=tk.LabelFrame(
            self.root,
            width=300,
            height=100,
            relief='flat'
        )
        bg_label=tk.Label(login_frame,image=self.lab_bg)
        user_name_lable = tk.Label(
            login_frame,
            text=u'头像越多时间越长!',
            fg='red',
            font=('黑体','10')
        )
        self.default_image=self.get_head_img_50x50(self.res_path,self.default_user_log)
        self.head_image_lable=tk.Label(
            login_frame,
            image=self.default_image,
            relief='raised'
        )
        self.user_name_value_lable=tk.Label(
            login_frame,
            text=u'登录后点击\'生成拼图\',并扫描二维码'
        )
        self.mix_logo_button=tk.Button(
            login_frame,
            state='disable',
            text=u'生成拼图',
            command=self.mix_logo
        )
        self.login_button=tk.Button(
            login_frame,
            text=u'登录',
            command=self.login_web
        )
        self.login_out_button=tk.Button(
            login_frame,
            text=u'退出',
            state='disable',
            command=self.login_out
        )
        #ui grid
        login_frame.grid(row=0, column=0)
        bg_label.place(x=0,y=0)
        user_name_lable.place(x=0, y=0)
        self.user_name_value_lable.place(x=52, y=40)
        self.mix_logo_button.place(x=175, y=0,width=60,height=20)
        self.login_button.place(x=255, y=0,width=40, height=20)
        self.head_image_lable.place(x=0,y=40,width=50,height=50)
        self.login_out_button.place(x=255, y=20,width=40, height=20)
    def close_window(self):
        # messagebox.showinfo('info','window close')
        try:
            itchat.logout()
        except Exception as e:
            pass
        self.root.destroy()
    def run_gui(self):
        self.root.protocol('WM_DELETE_WINDOW', self.close_window)
        self.root.mainloop()

if __name__=="__main__":
    a=ChatPy()
