# -*- coding: utf-8 -*-
# @Project : upupup 
# @Time    : 2018/5/25 16:43
# @Author  : 
# @File    : demo_ui.py
# @Software: PyCharm Community Edition
import tkinter as tk
from tkinter import scrolledtext
import paramiko

class Chat_UI():
    def __init__(self):
        self.root=tk.Tk()
        self.root.title('PyChat')
        self.root.geometry('800x600')
        self.user_name= tk.StringVar()
        self.password = tk.StringVar()
        self.teaching_path = tk.StringVar()


    def ui_grid(self,cntrl,row_column_tuple):
        cntrl.grid(row=row_column_tuple[0],column=row_column_tuple[1])
    def login_ssh(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        host_user_name=self.user_name.get()
        host_password=self.password.get()
        self.ssh.connect(hostname='10.16.3.26', port=22, username=host_user_name, password=host_password)

    def gitlog(self):
        cmd='cd {}'.format(self.teaching_path.get())
        cmd1='git log --color  --date=short  --pretty=format:"%h -%an- %ad -%s"'
        stdin, stdout, stderr = self.ssh.exec_command('{};{}'.format(cmd,cmd1)) #命令行需要在切换目录后马上执行不然会重新回到HOME目录，可能是session一样的原因
        print(stderr.readlines())
        all_outs=stdout.readlines()
        for x in all_outs:
            self.git_log_text.insert(tk.END, x)
    def ui_controls(self):
        logon_frame=tk.LabelFrame(self.root,width=300, height=80, text='登录')
        user_name_lable=tk.Label(logon_frame,text='user:')
        password_lable=tk.Label(logon_frame,text='password:')
        user_name_entry=tk.Entry(logon_frame,textvariable=self.user_name)
        password_entry=tk.Entry(logon_frame,textvariable=self.password,show='*')
        login_button=tk.Button(logon_frame,text='Login',command=self.login_ssh)
        #
        path_git_frame=tk.LabelFrame(self.root,width=700, height=80,text='path')
        teaching_lable = tk.Label(path_git_frame, text='teachong path:')
        git_log_button = tk.Button(path_git_frame, text='Git Log', command=self.gitlog)
        teaching_entry = tk.Entry(path_git_frame, textvariable=self.teaching_path)
        self.teaching_path.set('/data/javaweb/smart-city-education-teaching')
        #
        text_frame=tk.LabelFrame(self.root,width=700,height=400,text='日志')
        self.git_log_text=scrolledtext.ScrolledText(text_frame,wrap=tk.WORD)

        #
        logon_frame.grid(row=0,column=0)
        user_name_lable.place(x=0,y=0)
        user_name_entry.place(x=80,y=0)
        password_lable.place(x=0,y=20)
        password_entry.place(x=80,y=20)
        login_button.place(x=240,y=20,height=22)
        #
        path_git_frame.grid(row=1, column=0,columnspan=4)
        teaching_lable.place(x=0,y=0,width=100)
        teaching_entry.place(x=100,y=0,width=300)
        git_log_button.place(x=450,y=0,height=22)
        #
        text_frame.grid(row=4,columnspan=4)
        self.git_log_text.place(x=0,width=695,height=370)
    def run(self):
        self.ui_controls()
        self.root.mainloop()
if __name__ == '__main__':
    a=Chat_UI()
    a.run()
