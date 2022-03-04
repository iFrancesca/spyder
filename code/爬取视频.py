from bs4 import BeautifulSoup
import requests
import re

#re=<a href="https://tvshow.ku6.com/24695073" target="_blank">



#爬取页面代码并解析
def get_html(url):
    try:
        response=requests.get(url)
        response.raise_for_status
        response.encoding='utf-8'
        html=BeautifulSoup(response.text,'html.parser')
        return html
    except:
        print('爬取出错')

#Re爬取,得到视频链接和名称
def get_movie_url(html):
    image=re.compile(r'''<a href="(.*video.*id=.*)" target="_blank">(.*)</a>''')
    url_n_name=image.findall(str(html))
    _url=[]
    _name=[]
    for i in url_n_name:
        _url.append(i[0])
        _name.append(i[1])
    return _url,_name


#爬取视频网页的链接和名字
def main():
    url='https://www.ku6.com/index'
    html=get_html(url)
    movie_url,movie_name=get_movie_url(html)
    return movie_url,movie_name
u,n=main()

for i in range(len(u)):
    if u[i][0]=='h':
        continue
    else:
        u[i]='https://www.ku6.com/'+u[i]

