#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import  render_template
from app import create_app
from app.main.sa.decorated import user_login,user_only_login
from app.main.sa.models import *
from app.main.sa.persons import get_permission_list
app = create_app()


# 登入页面
@app.route('/')
def hello_world():
    return render_template('/system/login.html')


# 首页
@app.route('/welcome')
@user_only_login
def welcome():
    return render_template('page/welcome-1.html')


if __name__ == '__main__':

    # print(scheduler.get_jobs())
    app.run(host="0.0.0.0", port=8002, debug=True)
    # vehicle.to_zhixu_gongchengche()
