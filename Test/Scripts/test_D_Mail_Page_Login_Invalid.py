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
from src.PageObject.Pages.MailLoginPageValid import MailLoginValid
from src.PageObject.Pages.MailLoginPageInvalid import MailLoginInvalid
from Test.TestBase.WebDriverSetup import WebDriverSetup

class Onet_MailLoginPageInvalid(WebDriverSetup):

    def test_D_Mail_Page_Login_Invalid(self):
        self.homePage = Home(self.driver)
        try:
            self.homePage.permission_is_true()
        except Exception as error:
            print("Permission not find")
        self.emailPage = Mail(self.driver)
        self.emailPage.move_to_email_page()
        self.mailPageLogin = MailLoginValid(self.driver)
        self.mailPageLogin.is_email_form_located()
        self.mailPageLogin.insert_valid_email_name()
        self.mailPageInvalid = MailLoginInvalid(self.driver)
        try:
            self.mailPageInvalid.insert_invalid_pass()
        except Exception as error:
            print(error, "Fill invalid password - FAILED")

        self.mailPageLogin.login_remember_false()
        self.emailPage.submit_button()
        self.driver.execute_script("window.history.go(-1)")
        try:
            self.mailPageInvalid.insert_invalid_email()
        except Exception as error:
           print(error, "Fill invalid mail - FAILED") 

        self.mailPageLogin.insert_valid_pass()
        self.mailPageLogin.login_remember_false()
        self.emailPage.submit_button()

if __name__ == '__main__':
    unittest.main()