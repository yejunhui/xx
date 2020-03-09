#后台
from random import randint
import time
import pmysql

p = pmysql.pmysql()

#判断数据库是否存在
def init():
    it= []
    for item in p.msql('show tables;'):
        it.append(item[0])

    if 'users' not in it:
        p.msql('create table users (user text,name text,password text,email text,phone text,createDate double,oldDate double,ran double);')

#登录
def loginVerify(user,password):
    init()
    cont={}
    cont['In']= False
    sql = 'select user from users where user=\'%s\''%user
    ruser = p.msql(sql)
    if ruser != ():
        if user in ruser[0]:
            sql = 'select password from users where user=\"%s\";'%user
            rpassword = p.msql(sql)
            if password in rpassword[0]:
                ran = str(randint(0,99999999))
                sql = 'update users set ran=%s,oldDate=%s where user=\"%s\";'%(ran,time.time(),user)
                p.msql(sql)
                cont['In']= True
                cont['ran']= ran
                return cont
            else:
                return cont
        else:
            return cont
    else:
        return cont

#注册
def loginUpVerify(conts):
    init()
    cont= {}
    sql = 'select user from users where user=\'%s\''%conts['user']
    ruser = p.msql(sql)
    if ruser != ():
        if conts['user'] in ruser[0]:
            cont['In']= False
            return cont
    else:
        sql = 'insert into users (user,password,email,phone,name,createDate) values (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');'%(conts['user'],conts['password'],conts['email'],conts['phone'],conts['name'],str(time.time()))
        re = p.msql(sql)
        cont['In']= True
        cont['re']= re
        return cont

#在线验证
def index(user,ran):
    cont= {}
    init()
    sql= 'select ran from users where user=\"%s\";'%user
    sql2='select name from users where user=\"%s\";'%user
    ran2= p.msql(sql)[0][0]
    name= p.msql(sql2)[0][0]
    if ran == str(ran2):
        return True,name
    else:
        return True,None


#修改用户名
def user(user):
    init()
    sql = 'update users set ran=Null where user=\'%s\';'%(user)
    p.msql(sql)
#修改用户信息
def nowMod(conts):
    init()
    sql = 'update users set name=\'%s\',password=\'%s\',email=\'%s\',phone=\'%s\',ran=\'%s\' where user=\'%s\';'%(conts['name'],conts['password'],conts['email'],conts['phone'],conts['ran'],conts['user'])
    p.msql(sql)

def cls():
    p.cls()