#encoding=UTF-8

import pymysql
import sys
reload(sys)
sys.setdefaultencoding('utf8')
conn = pymysql.connect(user = 'root', passwd = '12345678', host = 'localhost', db = 'vou', charset = 'utf8')  
cur = conn.cursor()  
cur.execute("SELECT * FROM users")  
for r in cur:
    #print(r)
    #uname = str(r[3])
    print (  " id: "   + str(r[0]) 
           + " uid: "  + str(r[1])
           + " upwd: " + str(r[2])
           + " uname:" + r[3]
             #uname.decode('UTF-8').encode('GBK')
           )
cur.close()      
conn.close()  
print("conn: ",conn);  
