from flask import Flask
from flask import request

# 命令行中使用from test import app
# app.url_map 来查看URL映射
# URL中都有HEAD,OPTIONS,GET请求方法，其中HEAD,OPTIONS由路由flask自动处理


app=Flask(__name__)

# 处理URL和函数之间关系的程序成为路由
# 装饰器的惯用法是把函数注册为事件处理程序，再特定时间发生时调用
# 把index()函数注册为应用根地址的处理程序
@app.route('/')
def index():
    # 把request当作全局变量使用，使用上下文使request接受到的变量变为全局可访问
    # flask从客户端收到请求时，要让视图函数能访问一些对象，来处理请求
    # Flask 上下文全局变量 current_app g request session
    # request 请求对象，分装了客户端发出的http请求中的内容
    user_agent = request.headers.get('User-Agent') # 获取浏览器属性
    return '<h1>Your browser is {}</h1>'.format(user_agent)

# 使路由中的一部分可变 
# 路由URL中放在尖括号的内容就是动态部分，任何能匹配静态部分的URL都会映射到这个路由上 
# 调用试图函数时Flask会将动态部分作为参数传入函数
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=19722, debug=True)
    # 或者通过命令启动
    # export FLASK_APP=test.py
    # flask run
    # 开启调试模式 export FLASK_DEBUG=1
