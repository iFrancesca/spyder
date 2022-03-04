import requests
import json
import time
from lxml import etree

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
        
        html=response.text
       
        return html
    
    except:
        print('爬取出错')

#xpath解析
def parse_one_page(html):
    html=etree.HTML(html)
    index=html.xpath('/html/body/div[3]/div[1]/div/div[1]/ol/li/div/div[1]/em/text()')
    name=html.xpath('/html/body/div[3]/div[1]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
    DaA=html.xpath('/html/body/div[3]/div[1]/div/div[1]/ol/li/div/div[2]/div[2]/p[1]/text()')
    score=html.xpath('/html/body/div[3]/div[1]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]/text()')
    quote=html.xpath('/html/body/div[3]/div[1]/div/div[1]/ol/li/div/div[2]/div[2]/p[2]/span/text()')
    items=[]
    for i in range(len(name)):
        items.append((index[i],name[i],DaA[i],score[i],quote[i]))
    for item in items:
        yield{
            "index":item[0],
            "name":item[1],
            "DaA":item[2].strip(),
            "score":item[3],
            "quote":item[4]
        }
    return items

def write_to_file(content):
    with open("d:/python/爬虫/txt文件/豆瓣电影top_250.txt",'a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(offset):
    url= 'https://movie.douban.com/top250?start={}&filter='.format(str(offset))
    html=get_html(url)
    content=parse_one_page(html)
    for item in content:
        write_to_file(item)
        
for for i in range(10):
    main(i*25)
    time.sleep(1)



