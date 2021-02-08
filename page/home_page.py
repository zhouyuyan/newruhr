# -*- coding: utf-8 -*-
# @Time    : 2021/1/31 6:25 下午
# @Author  : zhouyy
# @FileName: home_page.py
# @Software: PyCharm
from appium.webdriver.common.mobileby import MobileBy
from page.base_page import BasePage
from page.search_temp import SearchTemp
from time import sleep


class HomePage(BasePage):
    def diaodu1(self):
        self._driver.find_element_by_xpath("//android.widget.TextView[@text='调度请求']").click()
        print("//android.widget.TextView[@text='调度请求']")
        sleep(5)

    def goto_search(self):
        sleep(5)
        self.find_element(MobileBy.XPATH, "//android.view.ViewGroup/android.widget.FrameLayout[2]").click()
        sleep(2)
        return SearchTemp(self._driver)
