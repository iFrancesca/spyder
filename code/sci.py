# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:24:10 2020

@author: syj
"""


import time
from selenium import webdriver

from selenium.webdriver.support.ui import Select
import random

browser = webdriver.Chrome()
url='http://apps.webofknowledge.com/Search.do?product=WOS&SID=6BkXugEPAJNcug4hzWZ&search_mode=AdvancedSearch&prID=9be86274-d6b8-4cb7-a598-dbb6822c3024'
url2='https://www.baidu.com'
browser.get(url)

'''
#打开浏览器，输入用户密码后开始工作
def browser_user_init(self):
        #打开浏览器
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    self.browser = webdriver.Chrome(chrome_options=options)
        #输入网址，登陆后开始工作
    self.browser.get("http://apps.webofknowledge.com/summary.do?product=WOS&doc=1&qid=7&SID=8Bvfh5aCeNiK3ekCfO4&search_mode=AdvancedSearch&update_back2search_link_param=yes")
        #确定能够检索数据
    input("确认登录了吗？按任意键继续！");

browser_user_init(url)
'''
