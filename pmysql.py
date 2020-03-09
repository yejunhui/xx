#本文件需要用到pymysql
import pymysql

class pmysql:
    def __init__(self,h='localhost',user='user',password='123456',db='uransData'):
        self.conn = pymysql.connect(host=h,user=user,password=password,db=db)
        self.conn.autocommit(True)
        self.cur = self.conn.cursor()


    def msql(self,sql):
        self.conn.ping(reconnect=True)
        self.cur.execute(sql)
        return self.cur.fetchall()

    def cls(self):
        self.cur.close()

