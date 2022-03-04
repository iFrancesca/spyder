# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:37:44 2020

@author: syj
"""


import requests
import json
import time
from lxml import etree
from fake_useragent import UserAgent

#/html/body/div/table[4]/tbody/tr/td/table/tbody/tr/td/p[1]/br[4]

'''
http://www.cssn.cn/zt/zt_xkzt/mkszyzt/jngcdxyfb170zn/ddlxyxy/dxpyxy/201802/t20180201_3836417.shtml
http://www.cssn.cn/lsx/lishixuezhuanti/bwcxljsm/lxzyls/jzm/201801/t20180104_3804467_1.shtml
6:http://www.cssn.cn/lsx/lishixuezhuanti/bwcxljsm/lxzyls/jzm/201801/t20180104_3804467_5.shtml
http://www.cssn.cn/lsx/lishixuezhuanti/bwcxljsm/lxzyls/jzm/201801/t20180104_3804467_9.shtml
'''

url=input('请输入链接：')
name=input('文档名字：')


#爬取页面代码并解析
def get_html(url):
    try:

        headers={'User-Agent':UserAgent().random,
                 'proxy':'114.225.246.117'}
        response=requests.get(url,headers=headers)
        response.raise_for_status
        response.encoding=response.apparent_encoding
        html=response.text                       #编码方式是gbk?或utf-8?
       
        return html
    
    except:
        print('爬取出错')
        


#xpath解析
def parse_one_page(html):
    html=etree.HTML(html)
    paragraph=html.xpath('//p//text()')

    return paragraph

def write_to_file(content):
    with open("d:/文档/{}.txt".format(name),'a',encoding='utf-8') as f:
        f.write(content)

def main():
    html=get_html(url)
    content=parse_one_page(html)
    write_to_file(url+'\n')
    for item in content:
        write_to_file(item+'\n')


main()
'''


url='http://cpc.people.com.cn/n1/2019/1106/c64094-31439558.html'
html=get_html(url)

content=parse_one_page(html)
print(content)
'''
