from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# 存储用户信息的字典
users = {
    '用户名': {'password': '密码', 'name_preference': '姓名+学号'},
    # 其他用户信息
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            return redirect(url_for('upload', username=username))
        else:
            return '登录失败，请重试'
    return render_template('login.html')

@app.route('/upload/<username>', methods=['GET', 'POST'])
def upload(username):
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename, ext = os.path.splitext(file.filename)
            new_filename = f"{users[username]['name_preference']}{ext}"
            file.save(os.path.join('uploads', new_filename))
            return '文件上传成功'
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
