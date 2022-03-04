from bs4 import BeautifulSoup
import requests
import re
import time
import threading
import queue as Queue
import random
import json
import csv

def get_page(url):
    User_Agent = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)'
    ]

    count = 0
    status_code = 403
    while status_code != 200:
        # 状态码不通过，sleep重新请求
        count += 1
        time.sleep(count*0.1)
        
        # 随机生成一个头部
        len_user_agent = len(User_Agent)
        random_num = random.randint(0, len_user_agent-1)
        user_agent = User_Agent[random_num]
        
        # 请求
        response = requests.get(url=url,headers={'User-Agent': user_agent})
        response.encoding = 'utf-8'
        
        # 得到html报文和状态码
        html = response.text
        status_code = response.status_code
        
    return html

url_lt = []
title_lt=[]
def get_book_url_list(html):
    soup = BeautifulSoup(html,'lxml')
    url_list_info = soup.find_all(class_ = 'pl2')
    pattern = re.compile('<a.*?href=(.*?)onclick=.*?title=(.*?)>.*?</a>',re.S)

    for url in url_list_info:
        url = str(url)
        url = re.search(pattern,url)
        url_lt.append(eval(url.group(1).strip()))
        title_lt.append(eval(url.group(2).strip()))

    return url_lt,title_lt




def get_comments(html_url):
    comments=[]
    urls=[html_url+'comments/hot?p={}'.format(str(i)) for i in range(1,5)]#多进程
    for url in urls:
        text=get_page(url)
        _comments_=re.findall(r"<span class=\"short\">(.*)</span>",text)
        for _comment_ in _comments_:
            comments.append(_comment_)
    return comments
    
def get_one_page(url_lt,title_lt):
    
    n=len(url_lt)
    items=[]
    for i in range(n):
        items.append((title_lt[i],get_comments(url_lt[i])))
    for item in items:
        yield{
            'title':item[0],
            'comments':item[1]
        }
    return items
    


def write_to_file(content):
    with open('d:/python/爬虫/文件/豆瓣图书_评论.csv','a',encoding='utf-8',newline='') as f:
        fieldnames=['title','comments']
        writer=csv.DictWriter(f,fieldnames=fieldnames)
        '''writer.writeheader()'''
        writer.writerows(content)
'''
content=[]
url = 'https://book.douban.com/top250?start=25'
html=get_page(url)
url_lt,title_lt=get_book_url_list(html)
items=get_one_page(url_lt,title_lt)
for item in items:
    content.append(eval(json.dumps(item,ensure_ascii=False)))
print(content)


'''
def main(offset):
    url = 'https://book.douban.com/top250?start=' + str(offset)
    html=get_page(url)
    url_lt,title_lt=get_book_url_list(html)    #得到该网页所有书的url-->html_0_lt
    items=get_one_page(url_lt,title_lt)
    for item in items:
        content.append(eval(json.dumps(item,ensure_ascii=False)))




if __name__=='__main__':
    a=time.perf_counter()
    content=[]
    for i in range(4,11):
        main(i*25)
        print('page'+str(i))
    write_to_file(content)
    b=time.perf_counter()
    print(b-a)











