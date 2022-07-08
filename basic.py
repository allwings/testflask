import json

from flask import Flask, request, redirect, render_template, Response, make_response, jsonify
from flask import url_for
from markupsafe import escape

app = Flask(__name__)


##01    basic
@app.route('/hello/<username>')
def hello(username):
    return f'Hello {username}!'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'


@app.route('/path/<path:path>')
def show_path(path):
    return f'path {escape(path)}'


##02+03+04
'''
@app.route('/')
def index():
    return render_template('welcome.html')
'''
'''
@app.route('/')
def index():
    int_ = 1024
    str_ = 'Hello World!'
    list_ = [1, 2, 3, 4, 5]                 # 列表数据
    dict_ = {'name': 'Kint', 'age': 23}      # 字典数据
    # render_template方法:渲染模板
    # 参数1: 模板名称  参数n: 传到模板里的数据
    return render_template('render_template.html', my_int=int_, my_str=str_, my_list=list_, my_dict=dict_)
'''

'''
@app.route('/login')
def login():
    print(f"in login function, request.values: {request.values}")
    return 'login'
'''


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


"""
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
"""


##03    http
@app.route('/welcome/<name>')
def welcome(name):
    return f'welcome {name}'

'''
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print("post")
        user = request.form['username']
        return redirect(url_for('welcome', name=user))
    else:
        print("get")
        user = request.args.get('username')  # GET方法获取数据，args是包含表单参数对及其对应值对的列表的字典对象。
        return redirect(url_for('welcome', name=user))
'''

## 04+05    json
'''
@app.route('/')
def index():
    return render_template("Request.html")
'''
@app.route('/login', methods=["GET", "POST"])
def login():
    print('request.method:\n', request.method)
    print('request.data:\n', request.data)
    print('request.request.args:\n', request.args)
    print("request.request.args.get('b'):\n", request.args.get('c'))
    print('request.form:\n', request.form)
    print("request.request.form.get('password'):\n", request.form.get('password'))  # 推荐使用request.form.get(key)避免关键词缺失而导致的KeyError
    print('request.values:\n', request.values)
    print('request.json:\n', request.json)
    print('request.cookies:\n', request.cookies)
    print('request.headers:\n', request.headers)
    return json.dumps(request.form)         # 将MultiDict数据处理为JSON数据


##05 cookie
@app.route('/')
def index():
    return redirect(url_for('set_cookie'))  # 重定向响应的URL

# 获取cookie
@app.route('/get_cookie')
def get_cookie():
    cookie = request.cookies.get('user')    # 获取关键字为user对应cookie的值
    print(cookie)
    return render_template('get_cookie.html', cookie=cookie)

# 设置cookie
@app.route('/set_cookie')
def set_cookie():
    html = render_template('show_cookie_by_JQuery.html')
    response = make_response(html)      # 设置响应体
    # response = Response(html)
    response.set_cookie('user', 'Kint')
    return response

# 删除cookie
@app.route('/del_cookie')
def del_cookie():
    html = render_template('show_cookie_by_JQuery.html')
    response = Response(html)
    response.delete_cookie('user')
    return response




if __name__ == '__main__':
    app.run(debug=True)
