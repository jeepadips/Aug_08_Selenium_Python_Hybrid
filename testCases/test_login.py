import time
from threading import Thread

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_homePageTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        time.sleep(25)
        act_title = self.driver.title
        if act_title == "OrangeHRM":
            assert True
            self.driver.close()
        else:
            assert False
            self.driver.close()


    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        time.sleep(25)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title == "OrangeHRM":
            assert True
            self.driver.close()
        else:
            assert False
            self.driver.close()






