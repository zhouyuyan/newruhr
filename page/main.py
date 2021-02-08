# -*- coding: utf-8 -*-
# @Time    : 2021/1/31 上午1:47
# @Author  : zhouyy
# @FileName: main.py
# @Software: PyCharm


from selenium.webdriver.common.by import By
from page.base_page import BasePage
from time import sleep
from page.home_page import HomePage
import logging


class Main(BasePage):

    def login(self, phone, password):
        logging.basicConfig(level=logging.INFO)
        sleep(2)
        self.find(By.XPATH, "//android.widget.EditText[@text='请输入您的手机号']").send_keys(phone)
        logging.info(phone)
        logging.info("hahahhaha")
        sleep(2)
        self.find(By.XPATH,
                  "//android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText[1]").send_keys(
            password)
        logging.info(password)

        sleep(2)
        self.find(By.ID, "ruhr.box:id/btnSubmit").click()
        sleep(2)
        return HomePage(self._driver)
