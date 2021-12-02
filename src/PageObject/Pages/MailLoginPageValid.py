import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
import os
sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

from Data.TestData import TestData
from src.PageObject.Locators import Locator
from src.PageObject.Pages.BasePage import Base

class MailLoginValid(Base):
    def __init__(self, drier):
        super().__init__(drier)
    
    def is_email_form_located(self):
       return self.is_element_located(Locator.email_form)    

    def login_remember_false(self):
        return self.click(Locator.login_remember)

    def insert_valid_email_name(self):
        self.driver.find_element(*Locator.email_form).clear()
        self.enter_text(Locator.email_form, TestData.valid_email_name)
        
    def insert_valid_pass(self):
            self.driver.find_element(*Locator.password_form).clear()
            self.enter_text(Locator.password_form,TestData.valid_pass)
    
    def is_user_mail_page_available(self):
           return self.is_element_located(Locator.user_page_available)

