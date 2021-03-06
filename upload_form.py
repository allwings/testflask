from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def student():
    return render_template('login.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form        # 拿到前端传输的表单数据
        return render_template("result.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
