from bs4 import BeautifulSoup
import re
import requests
import time
#将网页链接存到一个列表里
def url_list(n):
    l=[]
    for i in range(1,n+1):
        url='https://www.neihan8.com/article/list_5_'+str(i)+'.html'
        l.append(url)
    return l
#爬取网页内容
def get_html(url):
    try:
        response=requests.get(url)
        response.raise_for_status
        response.encoding=response.apparent_encoding
        html=response.text
        return html
    except:
        print('爬取失败')
#解析网页内容
def html_soup(html):
    html_soup=BeautifulSoup(html,'html.parser')
    html_str=str(html_soup)
    return html_str
def get_content(html_str):
    #提取相关内容
    content=re.compile(r'<a href="/article/\d*?\.html"><b>(.*?)</b></a>(.*?)<div class="f18 mb20">(.*?)</div>',re.S)
    t=content.findall(html_str)

    #将标题和正文提取出来
    result=[]
    for line in t:
        temp=[]
        for i in line:
            i=re.sub(r'\u3000|\n|<br>|<br/>|</h4>|\r|<p>|\ufffd|\xa0|\u200d','',i).strip()
            temp.append(i)
        result.append(temp)
    return result

#将提取的内容存储到文件中
def save_file(path,content):
    myFile=open(path,'a')
    for i in content:
        myFile.write('\n'+i[0]+'\n'+i[2]+'\n')
        myFile.write('-----------------over------------------')
    myFile.close()
def main():
    l=[]
    n=eval(input('请输入爬取页数:'))
    for url in url_list(n):
        html=get_html(url)
        html_str=html_soup(html)
        result=get_content(html_str)
        l.append(result)
    return l
path=input('请输入路径:')
a=time.perf_counter()
for i in main():
    save_file(path,i)
print('successful')
b=time.perf_counter()
print(b-a)

