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

class Mail(Base):
    def __init__(self, drier):
        super().__init__(drier)

    def move_to_email_page(self):
        return self.click(Locator.email_page)

    def is_email_page_loaded(self):
        return TestData.title_email_page in self.driver.title
    
    def submit_button(self):
         return self.click(Locator.submit_button)

