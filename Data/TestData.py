import sys
# import os
sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

class TestData():

    chrome_driver_path = "./chromedriver.exe"
    base_url = "https://www.onet.pl"
    title_homePage = "Onet"
    title_email_page = "Poczta"
    valid_email_name = "pythonselenium@onet.pl"
    valid_pass = "Python1234!"
    invalid_pass = "XYZ"
    invalid_email_name = "xyz@onet.pl"
    