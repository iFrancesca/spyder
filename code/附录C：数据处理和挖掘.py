url_info='https://node2d-public.hep.com.cn/41dc25357b75ae5aac8727bba1a0e6e8.pdf_files/41dc25357b75ae5aac8727bba1a0e6e8.pdf.files/{}.png'

url='https://ty.fang.lianjia.com/loupan/yingzequ/l2'
import requests
import csv
import time
from lxml import etree
from fake_useragent import UserAgent
import random



headers={'User-Agent':UserAgent().random}
response=requests.get(url,headers=headers)

headers={'User-Agent':UserAgent().random}
response=requests.get(url,headers=headers)
response.encoding=response.apparent_encoding
html=response.text
