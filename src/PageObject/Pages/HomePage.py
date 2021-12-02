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


class Home(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)
        

    def permission_is_true(self):
        return self.click(Locator.personal_data)

    def is_title_matches(self):
        return TestData.title_homePage in self.driver.title