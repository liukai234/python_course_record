# 自定义错误页面
# 404 客户端请求未知页面或路由
# 500 应用有未处理的异常

from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

app.run(host='0.0.0.0', port=19722)