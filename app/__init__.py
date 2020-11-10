# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 12:07
# @Author  : CongYiWei
# @Email   : 1056285392@qq.com
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask
from flask_migrate import Migrate
from app.config import config
from app.main.models import db


app = Flask(__name__)
# 创建数据库
migrate = Migrate()
app.config.from_object(config)
db.init_app(app)
migrate.init_app(app, db)


# 初始化app
def create_app():
    # 配置文件
    app.config.from_object(config)
    # 初始化数据库
    db.init_app(app)
    # 自定义的错误处理机制
    # 模板过滤器注册
    # 注册蓝图
    from app.main import main
    app.register_blueprint(main)
    return app

