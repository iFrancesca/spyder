import requests
import time
from lxml import etree
from fake_useragent import UserAgent
import csv
import random
#/html/body/div/table[4]/tbody/tr/td/table/tbody/tr/td/p[1]/br[4]

'''
http://www.cssn.cn/zt/zt_xkzt/mkszyzt/jngcdxyfb170zn/ddlxyxy/dxpyxy/201802/t20180201_3836417.shtml
http://www.cssn.cn/lsx/lishixuezhuanti/bwcxljsm/lxzyls/jzm/201801/t20180104_3804467_1.shtml
6:http://www.cssn.cn/lsx/lishixuezhuanti/bwcxljsm/lxzyls/jzm/201801/t20180104_3804467_5.shtml
http://www.cssn.cn/lsx/lishixuezhuanti/bwcxljsm/lxzyls/jzm/201801/t20180104_3804467_9.shtml
'''
'''
url=input('请输入链接：')
name=input('文档名字：')
r_url=input('请输入原始url:')
'''

url_r=input('请输入链接：')
limit=input('请输入limit:')
name=input('文档名字：')
n=eval(input('回答者有几人：'))//5


#爬取页面代码并解析
def get_html_json(url,offset):
    
    global limit
    try:
        data={
            "limit":limit,
            "offset":offset,
            "include":'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized,paid_info,paid_info_content;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics'
            }
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}
        response=requests.get(url,headers=headers,params=data)
        status_code=response.status_code
        count=0
        while status_code!=200:
            count+=1
            time.sleep(count*0.2)

            headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}
            response=requests.get(url,headers=headers,params=data)
            response.encoding=response.apparent_encoding
            
            return response.json()
        response.encoding=response.apparent_encoding
        return response.json()

    
    except:
        print('爬取出错')



#获取内容
def parse_one(html):
    html=etree.HTML(html)
    paragraphs=html.xpath('//p/text()')
    content=''
    for p in paragraphs:
        content+=p+'\n'

    return content

def write_to_file(content):
    global name
    with open("{}.csv".format(name),'a',encoding='utf-8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow([content])
        
        
def main(offset):
    js=get_html_json(url_r,offset)
    for item in js.get('data'):
        html=item.get('content')
        content=parse_one(html)
        write_to_file(content)

for i in range(n):
    main(i)
    time.sleep(random.random()*3)

'''
url='http://cpc.people.com.cn/n1/2019/1106/c64094-31439558.html'
html=get_html(url)

content=parse_one_page(html)
print(content)
'''

