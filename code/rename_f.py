# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:49:45 2020

@author: syj
"""

import os
#输入目标路径
path='C:\\Users\\syj\\Desktop\\党章\\'
#输入原名称 --新名称
nam=['page0', 'page2', 'page3', 'page4', 'page5', 'page6', 'page7', 'page8', 'page9', 'page10', 'page11', 'page12']
new_nam=['0','1党员','2组织制度','3中央组织','4地方组织','5基层组织','6党的干部','7党的纪律','8纪律检查机关','9党组','10共产主义青年团的关系','11党徽党旗']
pat=[]
new_pat=[]

def rename(path,name,new_name):
    old_file = os.path.join(path, name)
    new_file = os.path.join(path, new_name)
    os.rename(old_file, new_file)
    print(name)

for i in range(12):
    #输入后缀
    offset='.txt'
    rename(path,nam[i]+str(offset),new_nam[i]+str(offset))