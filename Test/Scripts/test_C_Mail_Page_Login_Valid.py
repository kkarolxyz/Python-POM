import unittest
import time
import sys
import os
sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

from selenium import webdriver
from selenium.webdriver.common.by import By
from Data.TestData import TestData
from src.PageObject.Pages.HomePage import Home
from src.PageObject.Pages.MailPage import Mail
from src.PageObject.Pages.MailLoginPageValid import MailLoginValid
from Test.TestBase.WebDriverSetup import WebDriverSetup

class Onet_MailLoginPageValid(WebDriverSetup):
    def test_C_Mail_Page_Login_Valid(self):
        self.homePage = Home(self.driver)
        try:
            self.homePage.permission_is_true()
        except Exception as error:
            print("Permission not find")
        self.emailPage = Mail(self.driver)
        self.emailPage.move_to_email_page()
        self.mailPageLogin = MailLoginValid(self.driver)
        try:
            self.mailPageLogin.is_email_form_located()
        except Exception as error:
            print(error, "MailPage: MailPage not located")
        try:
            self.mailPageLogin.insert_valid_email_name()
            self.mailPageLogin.insert_valid_pass()
        except Exception as error:
            print(error, "MailPage: Username or Password not insert")
        self.mailPageLogin.login_remember_false()
        try:
            self.emailPage.submit_button()
        except Exception as error:
            print(error, "MailPage: SubmitButton not found")
        self.mailPageLogin.is_user_mail_page_available()

            
if __name__ == '__main__':
    unittest.main()