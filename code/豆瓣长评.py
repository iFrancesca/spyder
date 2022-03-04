import requests
import csv
import time
from lxml import etree
from fake_useragent import UserAgent
import random


url_first=input('book/movie--url:')
offset=eval(input('评论页数:'))
name=input('书/影 名：')
choose=input('book or movie?')

 

#爬取页面代码并解析
def get_html(url):

    try:
        headers={'User-Agent':UserAgent().random}
        response=requests.get(url,headers=headers)
        status_code=response.status_code
        count=0
        while status_code!=200:
            count+=1
            time.sleep(count*0.1)

            headers={'User-Agent':UserAgent().random}
            response=requests.get(url,headers=headers)
            response.encoding=response.apparent_encoding
            html=response.text
            return html
        response.encoding=response.apparent_encoding
        html=response.text
        return html
    
    except:
        print('爬取出错')

#xpath解析
def get_id(html):
    html=etree.HTML(html)
    id=html.xpath('//div[@class="main review-item"]/@id')
    return id
    

#获得所有用户的id
id_lt=[]
def main1(offset):
    global url_first
    url= url_first+'?start={}'.format(str(offset))
    html=get_html(url)
    id=get_id(html)
    for i in id:
        id_lt.append(i)
        

for i in range(offset):
    try:
        main1(i*20)
        time.sleep(random.random()*3)
    except:
        print(url_first+'?start={}'.format(str(offset)))


def get_html_json(url):
    try:
        headers={'User-Agent':UserAgent().random}
        response=requests.get(url,headers=headers)
        status_code=response.status_code
        count=0
        while status_code!=200:
            count+=1
            time.sleep(count*0.2)

            headers={'User-Agent':UserAgent().random}
            response=requests.get(url,headers=headers)
            response.encoding=response.apparent_encoding
            
            return response.json()
        response.encoding=response.apparent_encoding
        return response.json()
    
    except:
        print('爬取出错_json')    
        
        
#xpath解析
def parse_one_page(html):
    html=etree.HTML(html)
    paragraphs=html.xpath('//p/text()')
    content=''
    for p in paragraphs:
        content+=p+'\n'

    return content


def write_to_file(content):
    global name
    with open("d:/文档/{}.csv".format(name),'a',encoding='utf-8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow([content])


def main2(id):
    global choose
    url= 'https://{}.douban.com/j/review/{}/full'.format(choose,id)
    js=get_html_json(url)
    html=js.get('html')
    content=parse_one_page(html)
    write_to_file(content)

for id in id_lt:
    try:
        main2(id)
        time.sleep(random.random()*3)
    except:
        print(id)







