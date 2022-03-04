N = eval(input('请输入要导出的题录总数：'))

n = N//500


for i in range(n):
    q = eval(input())
    i = q//500 
    a = 500*i +1
    b = 500*i + 500
    print(str(a)+'*********'+str(b))
   

13501-14000

14001-14500
