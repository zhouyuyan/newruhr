# -*- coding: utf-8 -*-
# @Time    : 2021/1/31 上午1:35
# @Author  : zhouyy
# @FileName: base_page.py
# @Software: PyCharm
from time import sleep

import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _driver: WebDriver
    _black_list=[(By.ID, "iv_close")]

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        try:
            element =  self._driver.find_element(locator, value)
            return element
        except:
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
            # 处理完黑名单后，再次找原来的元素
            return self.find(locator, value)
    def find_element(self,*loc):
        return self._driver.find_element(*loc)

