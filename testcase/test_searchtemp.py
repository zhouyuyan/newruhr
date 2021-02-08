# -*- coding: utf-8 -*-
# @Time    : 2021/1/31 6:02 下午
# @Author  : zhouyy
# @FileName: test_searchtemp.py
# @Software: PyCharm
from page.app import App

class TestSearchTemp(object):

    def setup(self):
        self.search=App().start().main().login("19090909090","19090909090").goto_search()

    def test_searchtemp(self):
        self.search.search()
    def test_detail(self):
        self.search.search().get_detail()
    # def teardown(self):
    #     App().quit()



