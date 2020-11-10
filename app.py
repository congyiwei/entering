# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 12:22
# @Author  : CongYiWei
# @Email   : 1056285392@qq.com
# @File    : app.py
# @Software: PyCharm
from app import create_app
app = create_app()


if __name__ == '__main__':
    app.run(debug=app.debug)
