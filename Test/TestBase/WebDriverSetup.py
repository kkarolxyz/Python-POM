import unittest
import urllib3

import sys
import os
sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

from time import sleep
from selenium import webdriver

from Data.TestData import TestData

class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(TestData.chrome_driver_path)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
 
    def tearDown(self):
        if (self.driver != None):
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()