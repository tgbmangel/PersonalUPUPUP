# -*- coding: utf-8 -*-
# @Project : upupup
# @Time    : 2018/5/7 17:08
# @Author  :
# @File    : mjtt.py
# @Software: PyCharm Community Edition

import requests
import re
import os


class Meiju():
    def __init__(self,home_url):
        self.home_url = home_url
        self.ed2k_url = re.compile('href="(ed2k.*?)"')
        self.coding_format='gbk'
    def get_download_url(self):
        # download_url_list=[]
        rsp=requests.get(self.home_url)
        rsp.encoding=self.coding_format
        HTML_content = rsp.text
        __all_download_re = re.findall(self.ed2k_url, HTML_content)
        return __all_download_re

if __name__=="__main__":
    home_url = "http://www.meijutt.com/content/meiju23109.html"
    A=Meiju(home_url)
    downloadurls=A.get_download_url()
    downloaded_list=os.listdir("F:\MeiJu")
    print("-"*50)
    print('已下载清单：')
    print(downloaded_list)
    print("-" * 50)
    os.chdir(r"D:\Program Files (x86)\Thunder Network\MiniThunder\Bin")
    for x in downloadurls:
        print("-" * 20)
        print('获取到：{}'.format(x))
        if x.split("|")[2] in downloaded_list:
            print("检测到已下载，跳过！")
        else:
            print("启动下载器！")
            os.system("start ThunderMini.exe -StartType:DesktopIcon \"%s\"" %x)
    print("-" * 50)
