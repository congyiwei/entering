# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 12:07
# @Author  : CongYiWei
# @Email   : 1056285392@qq.com
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Blueprint

main = Blueprint("main", __name__)

# 路由
from .views import index
