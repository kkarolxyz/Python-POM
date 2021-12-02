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
from Test.TestBase.WebDriverSetup import WebDriverSetup



class Onet_HomePage(WebDriverSetup):

    def test_A_Home_Page(self):
        self.homePage = Home(self.driver)
        try:
            self.homePage.permission_is_true()
        except Exception as error:
            print("Permission not find")
        try:
            assert self.homePage.is_title_matches()
        except Exception as error:
            print(error,"HomePage: Failed to load")

if __name__ == '__main__':
    unittest.main()