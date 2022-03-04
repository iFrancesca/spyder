n = 0
nn = 0
N = 0
f = open("univ.txt", "r")
univs = f.readlines()
for univ in univs:
    if "大学" in univ:
        n +=1
    if "学院" in univ:
        nn +=1
    if "学院"  and "学院" in univ:
        N +=1
f.close()

print("包含大学的名称数量是{}".format(n))
print("包含学院的名称数量是{}".format(nn))
print("包含大学和学院的名称数量是{}".format(N))


        
'''
from appiu import webdriver


server='http://localhost:4723/wd/hub'
desired_caps= {
  "platformName": "Android",
  "deviceName": "MI_8",
  "appPackage": "com.tencent.mm",
  "appActivity": ".ui.LauncherUI"
}
driver=webdriver.Remote(server,desired_caps)

el = driver. find_element_by_id(’ com.tencent.mm:id/cjk’)
el1 = driver.find_element_by_id("com.tencent.mm:id/bem")
el1.send_keys("18801032250")
el2 = driver.find_element_by_id("com.tencent.mm:id/dw1")
el2.click()

'''
'''
import pymysql

#声明一个MySQL连接对象db，传入运行的Host(即ip)
db=pymysql.connect(host='localhost',user='root',password='Jr7RW8Rt',port=3306)

#cursor()方法获得操作游标，利用游标来执行SQL语句
cursor=db.cursor()

#直接用execute()方法执行
cursor.execute('SELECT VERSION()')   #获得MySQL的当前版本

#fetchone()方法获得第一条数据
data=cursor.fetchone()
print('Datavase version:',data)
cursor.execute('CREATE DATABASE spider4 DEFAULT CHARACTER SET UTF8MB4')  #执行创建数据库的操作，数据库名叫soyders，默认编码为utf8
db.close()

'''
'''
import pymysql

db=pymysql.connect(host='localhost',user='root',password='Jr7RW8Rt',port=3306,db='spider4')
cursor=db.cursor()
sql='CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT  NULL, PRIMARY KEY (id))'
cursor.execute(sql)
db.close
'''

