import unittest
import time
import sys
import os
sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

from selenium import webdriver
from Data.TestData import TestData
from src.PageObject.Pages.HomePage import Home
from src.PageObject.Pages.MailPage import Mail
from Test.TestBase.WebDriverSetup import WebDriverSetup

class Onet_MailPage(WebDriverSetup):
    def test_B_Mail_Page(self):
        self.homePage = Home(self.driver)
        self.homePage.permission_is_true()
        self.emailPage = Mail(self.driver)
        self.emailPage.move_to_email_page()
        try:
            assert self.emailPage.is_email_page_loaded()
        except Exception as error:
            print(error,"MailPage: Failed to load")
            
if __name__ == '__main__':
    unittest.main()