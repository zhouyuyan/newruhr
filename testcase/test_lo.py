# -*- coding: utf-8 -*-
# @Time    : 2021/1/31 下午4:10
# @Author  : zhouyy
# @FileName: test_lo.py
# @Software: PyCharm
from page.app import App
import pytest,yaml

class TestLo():

    @pytest.mark.parametrize(("phone","password"), yaml.safe_load(open("/Users/zhouyuyan/PycharmProjects/newruhr/data/data_login1.yaml")))
    def test_ruhrlogin(self,phone,password):
        App().start().main().login(phone,password)
