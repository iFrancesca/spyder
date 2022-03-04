
name=input('请输入name:')
#输入要保存的文件名
ff=open('c:/Users/syj/Desktop/{}.txt'.format(name),'a',encoding='utf-8')
#输入迭代数
for i in range(2,13):
    #要合并的文件名
    with open('c:/Users/syj/Desktop/{}.txt'.format('page'+str(i)),'r',encoding='utf-8') as f:
        txt=f.read()
    ff.write(txt)
ff.close()
