from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort

app=Flask(__name__)

@app.route('/')
def index():
    # HTTP响应状态码 200成功处理 400请求无效
    # return '<h1>Bad Request</h1>', 400

    # 视图函数返回响应对象
    # response = make_response('<h1>This document carries a cookie!</h1>')
    # response.set_cookie('answer', '42')
    # return response

    # 重定向
    return redirect('http://liukai234.cn/')

@app.route('/user/<id>')
def get_user(id):
    user = False # 判断是否为假
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=19722, debug=True)
