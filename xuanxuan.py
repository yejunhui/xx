from datetime import timedelta

from flask import Flask, render_template, url_for, request, redirect, make_response, flash, send_from_directory
import back
import os


app= Flask(__name__)


#登录
@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    cont = {}
    user= request.form.get('user')
    password= request.form.get('password')
    re= back.loginVerify(user,password)
    if re['In']:
        resp= redirect(url_for('index'))
        resp.set_cookie('username',user)
        resp.set_cookie('ran',str(re['ran']))
        return resp
    else:
        return render_template('login.html',cont=cont)

#注册
@app.route('/loginUp')
def loginUp():
    cont= {}
    return render_template('loginUp.html',cont=cont)

#主页
@app.route('/index',methods=['GET','POST'])
def index():
    cont= {}
    cont['user']= user= request.cookies.get('username')
    cont['ran2']= ran2= request.cookies.get('ran')+'.0'
    cont['re'],cont['name']= back.index(user,ran2)
    if cont['re']:
        return render_template('myfamilyhome.html',cont=cont)
    else:
        return redirect(url_for('login'))



#个人页
@app.route('/my')
def myMes():
    cont = {}
    return render_template('myMes.html',cont=cont)

#退出
@app.route('/cls')
def cls():

    resp= make_response(redirect(url_for('login')))
    resp.delete_cookie('user')
    resp.delete_cookie('ran')
    #session.pop(request.cookies.get('user'))
    return resp

#启动
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)