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

class MailLoginInvalid(Base):
    def __init__(self, driver):
        super().__init__(driver)
    
    def insert_invalid_pass(self):
       self.driver.find_element(*Locator.password_form).clear()
       self.enter_text(Locator.password_form, TestData.invalid_pass)
    
    def insert_invalid_email(self):
        self.driver.find_element(*Locator.email_form).clear()
        self.enter_text(Locator.email_form, TestData.invalid_email_name)