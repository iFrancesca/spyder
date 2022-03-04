name=input('请输入name:')
ff=open('c:/Users/syj/Desktop/{}.txt'.format(name),'a',encoding='utf-8')
for i in range(1,6):
    with open('c:/Users/syj/Desktop/{}.txt'.format(i),'r',encoding='utf-8') as f:
        txt=f.read()
    ff.write(txt)
ff.close()
