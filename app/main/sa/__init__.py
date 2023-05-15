# _*_ coding:utf-8 _*_

from flask import Blueprint

system = Blueprint("system", __name__)


import app.main.sa.views # 必须放在这里，否则重复应用 

"""
系统管理模块
"""
