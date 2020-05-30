from flask import Flask
from flask import request

app = Flask(__name__)

# request 请求对象
# from 
# args
# values
# cookies
# headers
# files
# get_data()
# get_json()
# blueprint
# endpoint
# method
# scheme
# is_secure()
# host
# path
# query_string
# full_path
# url
# base_url
# remote_addr
# environ

# 请求钩子(狗子) (通过装饰器实现)
# before_request
# before_first_request
# after_request
# teardown_request

# 在钩子函数和视图函数之间共享数据使用上下文全局变量g
