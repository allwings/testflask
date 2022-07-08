import json

from flask import Flask, render_template, request, jsonify, Response

app = Flask(__name__)


# 1 接收参数，并返回json数据
@app.route('/sendDate', methods=['GET', 'POST'])
def form_data():
    # 从request中获取表单请求的参数信息
    title = request.form['title']
    datetime = request.form['datetime']
    quiz = request.form['quiz']

    # 此处逻辑代码已经省略...................

    return jsonify({'status': '0', 'errmsg': '登录成功！'})          # 1
    return json.dumps({'status': '0', 'errmsg': '登录成功！'},ensure_ascii=False)   #2
    # https://blog.csdn.net/u010197393/article/details/83503202

'''
data:"title="+data.field['title']+"&datetime="+data.field['datetime']+"&quiz="+data.field['quiz'],
'''

# 1
@app.route('/sendjson', methods=['POST'])
def sendjson():
    # 接受前端发来的数据
    data = json.loads(request.form.get('data'))
    # lesson: "Operation System" # score: 100 lesson = data["lesson"] score = data["score"]
    # 自己在本地组装成Json格式,用到了flask的jsonify方法
    # info = dict()
    # info['name'] = "pengshuang"
    # info['lesson'] = lesson
    # info['score'] = score
    # return jsonify(info)
'''
<script>    利用flask的request.form.get方法，获得前端发送给后台的json文件
    $(document).ready(
    function () { 
    var data = { data: JSON.stringify({"lesson": "Operation System", "score": 100}) } 
    $.ajax({ url:"/sendjson", type: 'POST', data: data, success: function (msg) { alert(msg.name) } }) 
    }); 
</script> 
'''

# 2
@app.route('/sendjson2', methods=['POST'])
def sendjson2():
    # 接收前端发来的数据,转化为Json格式,我个人理解就是Python里面的字典格式
    data = json.loads(request.get_data())

    # 然后在本地对数据进行处理,再返回给前端
    '''name = data["name"] age = data["age"] location = data["location"] data["time"] = "2016" '''
    # Output: {u'age': 23, u'name': u'Peng Shuang', u'location': u'China'}
    # print data return jsonify(data)

''' 这一种更常见也更容易理解一些，在前端组织好Json，再传递给后台
<script>
    $(document).ready(function () 
    { var student = new Object(); student.name = "Peng Shuang"; student.age = 23; student.location = "China"; 
    var data = JSON.stringify(student) 
    .ajax({ url: "/sendjson2", type: "POST", data: data, success: function (msg) { alert(msg.time) } }) }) 
</script>
'''

# 2 如果POST的数据是JSON格式，request.json会自动将json数据转换成Python类型（字典或者列表）
@app.route('/add', methods=['POST'])
def add():
    print(request.headers)
    print(type(request.json))
    print(request.json)

    result = request.json['a'] + request.json['b']
    return str(result)
    # 响应JSON时，除了要把响应体改成JSON格式，响应头的Content-Type也要设置为application/json
    result = {'sum': request.json['a'] + request.json['b']}
    return Response(json.dumps(result),  mimetype='application/json')



if __name__ == '__main__':
    app.run(debug=True)