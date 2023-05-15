# _*_ coding: utf-8 _*_

from flask import session, redirect, request, abort
from functools import wraps
from app.main.sa.persons import get_permission_list
from app.main.sa import salog 


# 登录装饰器(验证是否已登录和是否有权限访问)
def user_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" not in session:  # 未登录则跳转登录页
            return redirect('/')
        else:
            salog.save_log('sa模块','登入页面','测试使用_用户登入了当前页面')
            if 'permission' in session:
                per = session['permission']
            else:
                per = get_permission_list(session['user_id'])
                session['permission'] = per  
            if request.path not in session['permission']:
                session.pop('permission')
                abort(403)  # 返回没有访问权限的错误
        return f(*args, **kwargs)
    return decorated_function


# 登录装饰器(验证是否已登录,对数据获取限制)
def user_only_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:  # 未登录则跳转登录页
            return redirect('/')
        salog.save_log('sa模块','操作数据','测试使用_用户操作了数据')
        return f(*args, **kwargs)
    return decorated_function
