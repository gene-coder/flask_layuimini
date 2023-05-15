# _*_ Coding:utf-8 _*_

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.main.common.file_op import readfile

db = SQLAlchemy()


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 实例化SQLAlchemy
db = SQLAlchemy()
# PS : 实例化SQLAlchemy的代码必须要在引入蓝图之前


def create_app():
    app = Flask(__name__)
    app.secret_key = 'fkdjsafjdkfdlkjfadskjfadskljdsfklj'
    app.config['SECRET_KEY'] =  'fkdjsafjdkfdlkjfadskjfadskljdsfklj'
    # 初始化App配置 这个app配置就厉害了,专门针对 SQLAlchemy 进行配置
    # SQLALCHEMY_DATABASE_URI 配置 SQLAlchemy 的链接字符串儿
    database = readfile('./app/conf/main.ini','ini')['appuser']
    # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://appuser:comeon@127.0.0.1:3306/appuser?charset=utf8"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".\
        format(database['datausr'],database['datapwd'],database['dataip'],database['dataport'],database['database'])
    
    app.config["SQLALCHEMY_POOL_SIZE"] = 5 #配置 SQLAlchemy 的连接池大小
    app.config["SQLALCHEMY_POOL_TIMEOUT"] = 15  # 配置 SQLAlchemy 的连接超时时间
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # 初始化SQLAlchemy , 本质就是将以上的配置读取出来
    db.init_app(app)
    from app.main.sa import system 
    app.register_blueprint(system,url_prefix='/system') #系统管理

    return app
