for # -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 18:21:55 2020

@author: syj
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from lxml import etree
import json
import csv

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

browser=webdriver.Chrome()
wait=WebDriverWait(browser,10)
browser.get('https://s.taobao.com/search?q=iPad')
                                 

          
def index_page(page):
    print('正在爬取',page,'页')
    try:
        if page>1:
            input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input')))
            button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))               
            input.clear()
            input.send_keys(page)
            button.click() 
        wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input'))
                 )
        wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit'))
                )
        get_products(page)
    except TimeoutException:
        index_page(page)



def get_products(page):
    '''
    提取商品数据
    '''
    html=browser.page_source
    html=etree.HTML(html)
    item=html.xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[1]')
    for i in range(1,45):
        product={
                'image':'https:'+item[0].xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[{}]/div[1]/div/div[1]/a/img/@data-src'.format(i))[0],
                'title':item[0].xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[{}]/div[1]/div/div[1]/a/img/@alt'.format(i))[0],
               'location':item[0].xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[{}]/div[2]/div[3]/div[2]/text()'.format(i)),
               'price':item[0].xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[{}]/div[2]/div[1]/div[1]/strong/text()'.format(i))[0],
               'shop':item[0].xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[{}]/div[2]/div[3]/div[1]/a/span[2]/text()'.format(i)),
               'deal':item[0].xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[{}]/div[2]/div[1]/div[2]/text()'.format(i))
               }
        print(i,end=' ')
        save_to_file(product)
def save_to_file(content):
    try:
        with open('d:/python/爬虫/文件/淘宝商品_iPad.csv','a',encoding='utf-8',newline='') as f:
            json_s=json.dumps(content,ensure_ascii=False)    #type(json)=str
            fieldnames=['image','title','location','price','shop','deal']
            writer=csv.DictWriter(f,fieldnames=fieldnames)
            writer.writerow(eval(json_s))
    except:
        print('保存失败')
        
def main():
    for i in range(20):
        index_page(i)
        time.sleep(2)

main()