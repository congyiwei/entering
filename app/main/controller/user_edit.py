# -*- coding: utf-8 -*-
# @Time    : 2020/11/10 9:06
# @Author  : CongYiWei
# @Email   : 1056285392@qq.com
# @File    : user_edit.py
# @Software: PyCharm

from app.main.models import Tester, db

from app import app


def edit(name, phone, address, sex):
    with app.app_context() as ctx:
        tester = Tester(name=name, phone=phone, address=address, sex=sex)
        db.session.add(tester)
        db.session.commit()
    return "success"
