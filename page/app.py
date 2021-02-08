# -*- coding: utf-8 -*-
# @Time    : 2021/1/31 上午1:36
# @Author  : zhouyy
# @FileName: app.py
# @Software: PyCharm
import yaml
from appium import webdriver

from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    _package = "ruhr.box"
    _activity ="ruhr.box.work.other.SplashAct"
    def start(self):
        if self._driver is None:
            caps = dict()
            caps["platformName"] = "android"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = False
            # caps['udid'] = yaml.safe_load(open("../page/configuration.yaml"))['caps']['udid']
            # 初始化driver
            self._driver = webdriver.Remote(
                "http://localhost:4723/wd/hub",
                caps)

        else:
            self._driver.start_activity(self._package, self._activity)
        self._driver.implicitly_wait(5)
        return self

    def quit(self):
        self._driver.quit()
        return self

    def main(self) -> Main:
        return Main(self._driver)
