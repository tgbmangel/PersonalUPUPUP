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

h=BeautifulSoup(HTML_content,'lxml')
ls=h.find_all('a',href=re.compile('ed2k'))
for x in ls:
    print(x)
    print(x.attrs['href'])

A=re.findall(ed2k_url,HTML_content)
for x in A:
    print(x)
'''
os.chdir("D:\Program Files (x86)\Thunder Network\Thunder\Program\") 

os.system("Thunder.exe -StartType:DesktopIcon "%s"" % a) 
'''

class Meiju():
    def __init__(self,home_url):
        self.home_url = home_url
        self.ed2k_url = re.compile('href="(ed2k.*?)"')
        self.coding_format='gbk'
    def get_download_url(self):
        rsp=requests.get(self.home_url)
        rsp.encoding=self.coding_format
        HTML_content = rsp.text
