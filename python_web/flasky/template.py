# flask extenion
# Jinja2 模板引擎

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 使用的默认路径是 ./templates/index.html
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    # 左边的参数表示模板中使用的占位符，右边表示当前作用域中的变量
    # 两边使用相同的变量名很常见，但不是强制要求
    return render_template('user.html', name = name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=19722, debug=True)