# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:32:24 2020

@author: syj
"""

'''
https://movie.douban.com/subject/27619748/comments?status=F
https://movie.douban.com/subject/27619748/comments?start=20&limit=20&sort=new_score&status=F
https://movie.douban.com/subject/27619748/comments?start=40&limit=20&sort=new_score&status=F
'''

import requests

import time
from lxml import etree
from fake_useragent import UserAgent
import random



#爬取页面代码并解析
def get_html(url):

    try:
        headers={'User-Agent':UserAgent().random,
                 #cookies必须输入
                 'Cookie':'bid=UkPULinHwvY; douban-fav-remind=1; __gads=ID=c410bd4f2d510124:T=1567726936:S=ALNI_Ma0A1dwTpk_RA7LpfSjbV46XsyydA; __utma=30149280.539221959.1569569226.1583069333.1583160224.45; __utmz=30149280.1583160224.45.26.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; viewed="3486336_30390658_1451628_30259677_33406377_33379779_34872361_33657946_6131276_2209691"; gr_user_id=53699f45-d781-48d7-85e8-1c7171626c38; _vwo_uuid_v2=D8630471F505EF38F8CA78D674F81FC51|bff3a2f9a575008854079d2dead53062; ll="108288"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1583069333%2C%22https%3A%2F%2Fbook.douban.com%2Fsubject%2F1090043%2Freviews%22%5D; _pk_id.100001.4cf6=526c27dfd2aec202.1569569225.21.1583069812.1582982242.; __utma=223695111.649937195.1569569226.1582981994.1583069333.22; __utmz=223695111.1582981994.21.13.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=6JKdyR2BdfXcfvDrMilwYouOn6MJY67n; trc_cookie_storage=taboola%2520global%253Auser-id%3D6959b9e4-208e-4cb7-b744-aa00e1bfcbab-tuct4873f53; __utmv=30149280.19051; ct=y; push_noty_num=0; push_doumail_num=0; ap_v=0,6.0; dbcl2="215628392:DZgxIoFbHac"; ck=paOq'}
        response=requests.get(url,headers=headers)
        status_code=response.status_code
        count=0
       
        while status_code!=200:
            count+=1
            time.sleep(count*0.1)

            headers={'User-Agent':UserAgent().random,
                     #cookies必须输入
                     'Cookie':'bid=UkPULinHwvY; douban-fav-remind=1; __gads=ID=c410bd4f2d510124:T=1567726936:S=ALNI_Ma0A1dwTpk_RA7LpfSjbV46XsyydA; __utma=30149280.539221959.1569569226.1583069333.1583160224.45; __utmz=30149280.1583160224.45.26.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; viewed="3486336_30390658_1451628_30259677_33406377_33379779_34872361_33657946_6131276_2209691"; gr_user_id=53699f45-d781-48d7-85e8-1c7171626c38; _vwo_uuid_v2=D8630471F505EF38F8CA78D674F81FC51|bff3a2f9a575008854079d2dead53062; ll="108288"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1583069333%2C%22https%3A%2F%2Fbook.douban.com%2Fsubject%2F1090043%2Freviews%22%5D; _pk_id.100001.4cf6=526c27dfd2aec202.1569569225.21.1583069812.1582982242.; __utma=223695111.649937195.1569569226.1582981994.1583069333.22; __utmz=223695111.1582981994.21.13.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=6JKdyR2BdfXcfvDrMilwYouOn6MJY67n; trc_cookie_storage=taboola%2520global%253Auser-id%3D6959b9e4-208e-4cb7-b744-aa00e1bfcbab-tuct4873f53; __utmv=30149280.19051; ct=y; push_noty_num=0; push_doumail_num=0; ap_v=0,6.0; dbcl2="215628392:DZgxIoFbHac"; ck=paOq'}
            response=requests.get(url,headers=headers)
            html=response.text
            return html
        
        
        html=response.text
        return html
    
    except:
        print('爬取出错')


#xpath解析
def parse_one_page(html):
    html=etree.HTML(html)
    #输入具体的xpath
    comments=html.xpath('//span[@class="short"]/text()')
    
    return comments
    


def write_to_file(content):
    #输入保存路径
    with open('d:/python/spyder/文件/豆瓣电影_评论.txt','a',encoding='utf-8') as f:
        f.writelines(content)
        
        
'''

url = 'https://movie.douban.com/subject/27619748/comments?start=0&limit=20&sort=new_score&status=F'
html=get_html(url)
comments=parse_one_page(html) 
write_to_file(comments)


'''
def main(offset):
    #初始url
    url = 'https://movie.douban.com/subject/27619748/comments?start={}&limit=20&sort=new_score&status=F' .format(offset)
    html=get_html(url)
    comments=parse_one_page(html) 
    write_to_file(comments)
    if comments==[]:
        print('*'*50)


if __name__=='__main__':
    a=time.perf_counter()
    for i in range(10,269):   #5380条短评
        main(i*20)
        time.sleep(random.randint(0,5)*random.random())
        print('page'+str(i+1))
    b=time.perf_counter()
    print(b-a)
