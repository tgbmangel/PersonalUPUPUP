# -*- coding: utf-8 -*-
# @Project : upupup 
# @Time    : 2018/5/7 17:08
# @Author  : 
# @File    : mjtt.py
# @Software: PyCharm Community Edition

import requests
import re

#home_url="http://www.meijutt.com/content/meiju23109.html"
home_url="http://www.meijutt.com/content/meiju22434.html"
ed2k_url=re.compile('href="(ed2k.*?)"')
p=requests.get(home_url)
p.encoding='gbk'
print(p.encoding)
HTML_content=p.text

A=re.findall(ed2k_url,HTML_content)
for x in A:
    print(x)

class Meiju():
    def __init__(self,home_url):
        self.home_url = home_url
        self.ed2k_url = re.compile('href="(ed2k.*?)"')
        self.coding_format='gbk'
    def get_url(self):
        r=requests.get(self.home_url)
