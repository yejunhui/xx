#本文件需要用到pymysql
import pymysql

class pmysql:
    def __init__(self,h='w.rdc.sae.sina.com.cn',user='xnl0zzw55m',password='2w051l1wy22y12i5xm5ly3mhyi03jw35zy402543',db='app_gold'):
        self.conn = pymysql.connect(host=h,user=user,password=password,db=db)
        self.conn.autocommit(True)
        self.cur = self.conn.cursor()


    def msql(self,sql):
        self.conn.ping(reconnect=True)
        self.cur.execute(sql)
        return self.cur.fetchall()

    def cls(self):
        self.cur.close()

