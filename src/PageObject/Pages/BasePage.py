import time
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
# import os
sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

from Data.TestData import TestData
from src.PageObject.Locators import Locator


class Base():
    def __init__(self, driver):
        self.driver = driver
    
    def click(self, by_locator):
       WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by_locator))).click()

    def is_element_located(self, by_locator):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(by_locator))
    
    def enter_text(self,by_locator, send_text):
        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(by_locator)).send_keys(send_text)


