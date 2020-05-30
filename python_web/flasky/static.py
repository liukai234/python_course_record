# 静态文件
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# 通过路由处理页面间的跳转
@app.route('/r404/')
def r404():
    return render_template('404.html')

app.run(host='0.0.0.0', port=19722)