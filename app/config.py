# -*- coding: utf-8 -*-
# @Time    : 2020-10-24 22:33
# @Author  : CongYiWei
# @Email   : 1056285392@qq.com
# @File    : config.py
# @Software: PyCharm
from flask import Flask

app = Flask(__name__)


class BaseConfig:
    PER_PAGE = 10
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/tester'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProdConfig(BaseConfig):
    pass


class TestConfig(BaseConfig):
    DEBUG = True


config = DevelopmentConfig()

