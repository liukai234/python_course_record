# 参考书籍：《Flask Web开发：基于Python的Web应用开发环境（第2版）》
## pip国内镜像源
- -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
## 创建虚拟环境
- python -m venv venv-virtual-name
## 激活虚拟环境
- source venv/bin/activate
## 退出虚拟环境
- deactivate
## 调整包搜索路径到虚拟环境中
- 更改PYTHONPATH环境变量
- export PYTHONPATH=$PYTHONPATH:/home/lk234/pyFile/python_web/flasky/venv/lib/python3.6/site-packages
- 检查$PATHONPATH中是否有增加的路径
- [注] 仅适用于当前终端