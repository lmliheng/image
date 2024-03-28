# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# 设置应用的秘钥，用于加密 session 数据
app.secret_key = 'hjsbabjdcabw'

# 假设这是您的用户数据存储
users = {
    "admin": "123",
    "user": "123",
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            # 将用户名存储在 session 中
            session['username'] = username
            return redirect(url_for('profile', username=username))
        else:
            return "抱歉：用户名或密码错误"

    return render_template('login.html')

@app.route('/profile/<username>')
def profile(username):
    # 检查用户是否已登录
    if 'username' not in session or session['username'] != username:
        # 如果用户未登录，重定向用户回登录页面
        return redirect(url_for('login', next=request.url))

    return render_template('profile.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
    # 注意部署的时候要更改这里的参数，自行修改
    # 如app.run(host='0.0.0.0', port=80)