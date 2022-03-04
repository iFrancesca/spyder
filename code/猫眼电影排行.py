from bs4 import BeautifulSoup
import requests
import re
import json
import time
#re=<a href="https://tvshow.ku6.com/24695073" target="_blank">

#爬取页面代码并解析
def get_html(url):
    try:
        headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
            }
        proxies={
                "http": "117.90.0.225:9000"
            }
        response=requests.get(url,headers=headers,proxies=proxies,timeout=1)
        response.raise_for_status
        response.encoding='utf-8'
        
        html=BeautifulSoup(response.text,'html.parser')
       
        return html
    
    except:
        print(url,'爬取出错')
        

#Re正则提取
def parse_one_page(html):
    pattern=re.compile(
        '<dd>.*?class="board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?title.*?>(.*?)</a>.*?'+
        'star.*?>(.*?)<.*?releasetime.*?>(.*?).*?<.*?<i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>.*?</dd>',re.S
    )
    items=re.findall(pattern,str(html))   #注意将html转化为str格式
    for item in items:
        yield{
                "index":item[0],
                "image":item[1],
                "name":item[2],
                "star":item[3].strip()[3:],
                "releasetime":item[4].strip()[5:],
                "integer":item[5]+item[6],
        }
    return items


#写入文件
def write_to_file(content):
    path='d:/python/爬虫/猫眼电影排行.txt'
    with open(path,'a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

#整合代码
def main(offset):
    url='https://maoyan.com/board/4?offset='+str(offset)
    html=get_html(url)
    items=parse_one_page(html)
    for item in items:
        write_to_file(item)


for i in range(10):
    main(offset=10*i)
    time.sleep(1)

