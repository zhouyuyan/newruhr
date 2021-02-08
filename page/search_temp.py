# -*- coding: utf-8 -*-
# @Time    : 2021/1/31 5:55 下午
# @Author  : zhouyy
# @FileName: search_temp.py
# @Software: PyCharm
from appium.webdriver.common.mobileby import MobileBy
from page.base_page import BasePage
from page.temp_detail import TempDetail


class SearchTemp(BasePage):
    def search(self):
        ele=self.find(MobileBy.ID,'ruhr.box:id/et_search')
        ele.click()
        ele.send_keys("8010600000292")
        self.find(MobileBy.ID,'ruhr.box:id/tvSearch').click()
        return TempDetail(self._driver)

