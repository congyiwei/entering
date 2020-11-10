# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 12:07
# @Author  : CongYiWei
# @Email   : 1056285392@qq.com
# @File    : __init__.py.py
# @Software: PyCharm
import time

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    # 不生成表
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.Integer, default=int(time.time()))
    update_time = db.Column(db.Integer, default=int(time.time()), onupdate=int(time.time()))
    status = db.Column(db.SmallInteger, default=1)


class Tester(Base):
    name = db.Column(db.String(30), nullable=False, default='', unique=True)
    phone = db.Column(db.String(11))
    sex = db.Column(db.String(10))
    address = db.Column(db.String(10))

