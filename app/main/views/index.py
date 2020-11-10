# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 12:23
# @Author  : CongYiWei
# @Email   : 1056285392@qq.com
# @File    : index.py
# @Software: PyCharm
from flask import render_template, request
from app.main import main


@main.route("/")
def index():
    return render_template('index.html')


@main.route("/submit", methods=['POST'])
def connection():
    json_data = request.data.decode()
    name = eval(json_data)["name"]
    phone = eval(json_data)["phone"]
    address = eval(json_data)["address"]
    sex = eval(json_data)["sex"]
    from app.main.controller.user_edit import edit
    try:
        edit(name, phone, address, sex)
        return {"status": "success", "message": "提交成功"}
    except:
        return {"status": "faild", "message": "提交失败，请修改信息后重试"}