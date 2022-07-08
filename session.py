from flask import Flask, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'abc'

# 与Cookie不同，Session数据存储在服务器上，用来存储用户的信息 (例如登录状态、用户名称)
# Session 有一个唯一标识 ID，对应一个用户，在服务端使用 ID 可以查找到对应用户的数据，故Flask应用程序需要一个定义的密钥SECRET_KEY
@app.route('/')
def index():
    if 'user' in session:
        # 获取会话中的用户信息
        user = session.get('user')
        return '登录用户是:' + user + '<br>' + "<b><a href = '/logout'>点击这里注销</a></b>"
    return "<h3>暂未登录</h3><br>" + "<a href = '/login'></b>点击这里登录</b></a>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 设置会话中的用户信息
        session['user'] = request.form['user']
        return redirect(url_for('index'))
    return
    '''
    <form action="" method="post">
        <p><input type="text" name="user"/></p>
        <p><input type="submit" value="登录"/></p>
    </form>
    '''

@app.route('/logout')
def logout():
    # 删除会话中的用户信息
    session.pop('user')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
