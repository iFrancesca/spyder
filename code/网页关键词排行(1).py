import requests
from bs4 import BeautifulSoup
import jieba
    
    
#爬取页面代码并解析
def get_html(url):
    try:
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}
        response=requests.get(url,headers=headers)
        response.raise_for_status
        response.encoding=response.apparent_encoding
        html=BeautifulSoup(response.text,'html.parser')
        return html
    except:
        print('爬取出错')


#计算关键词出现次数
def count_word(txt):
    counts={}
    words=jieba.cut(txt)
    for word in words:
        if len(word)==1:
            continue
        else:
            counts[word]=counts.get(word,0)+1
    return counts


def main():
    url=input('请输入网址：')
    html=get_html(url)
    print('get html')
    t=html.get_text('+',strip=True)
    txt = "".join(i for i in t if ord(i) >= 256)  #txt中除去英文
    print('get txt')
    counts=count_word(txt)
    items=list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)
    for i in range(15):
        word,count=items[i]
        print('{:<15}{:>5}'.format(word,count))
main()
