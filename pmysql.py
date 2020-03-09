#本文件需要用到pymysql
import pymysql

h1='w.rdc.sae.sina.com.cn'
user1='xnl0zzw55m'
password1='2w051l1wy22y12i5xm5ly3mhyi03jw35zy402543'
db1='app_gold'

class pmysql:
    def __init__(self,h='localhost',user='user',password='123456',db='uransData'):
        self.conn = pymysql.connect(host=h1,user=user1,password=password1,db=db1)
        self.conn.autocommit(True)
        self.cur = self.conn.cursor()


    def msql(self,sql):
        self.conn.ping(reconnect=True)
        self.cur.execute(sql)
        return self.cur.fetchall()

    def cls(self):
        self.cur.close()

