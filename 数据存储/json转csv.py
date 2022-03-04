import csv


with open('d:/python/爬虫/txt文件/猫眼电影排行.txt','r',encoding='utf-8') as f:
       fieldnames='''['index','image','name','star','releasetime','integer']'''
       items=f.readlines()
       content=[]
       for item in items:
           content.append(eval(item.strip()))
       
with open('''d:/python/爬虫/txt文件/猫眼电影排行.csv''','a',encoding='utf-8',newline='') as ff:
    writer=csv.DictWriter(ff,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(content)
