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
@app.route('/loginUp',methods=['GET','POST'])
def loginUp():
    cont = {}
    if request.method == 'POST':
        cont['password'] = request.form['password']
        if cont['password'] == request.form['password2']:
            cont['user'] = request.form['user']
            cont['name'] = request.form['name']
            cont['email'] = request.form['email']
            cont['phone'] = request.form['phone']
            cont = back.loginUpVerify(cont)
            if cont['In']:
                return redirect(url_for('login'))
            else:
                return render_template('loginUp.html')
    else:
        return render_template('loginUp.html')

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



# 个人信息
@app.route('/my', methods=['GET', 'POST'])
def myMes():
    cont = {}
    cont['user']= user= request.cookies.get('username')
    cont['ran2']= ran2= request.cookies.get('ran')+'.0'
    cont['re'],cont['name']= back.index(user,ran2)
    if cont['re']:
        return render_template('myMes.html', cont=cont)
    else:
        return redirect(url_for('login'))


# 个人信息修改
@app.route('/vMyMes', methods=['GET', 'POST'])
def vMyMes():
    cont = {}
    cont['user']= user= request.cookies.get('username')
    cont['ran2']= ran2= request.cookies.get('ran')+'.0'
    cont['re'],cont['name']= back.index(user,ran2)
    if 'v' in request.args:
        cont['v'] = request.args.get('v')
    if cont['re']:
        if request.method == 'POST':
            if 'name' in request.form:
                cont['name'] = request.form['name']
                cont['email'] = request.form['email']
                cont['phone'] = request.form['phone']
            if 'password' in request.form:
                if request.form['password'] == cont['password'] and request.form['npassword'] == request.form[
                    'npassword2']:
                    cont['password'] = request.form['npassword']
            back.nowMod(cont)
            return redirect(url_for('myMes'))
        else:
            if 'v' in request.args:
                cont['v'] = cont['t'] = request.args['v']
                return render_template('vMyMes.html', cont=cont)
            else:
                return redirect(url_for('myMes'))
    else:
        return redirect(url_for('login'))

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
    app.run(host='0.0.0.0',port=5050,debug=True)