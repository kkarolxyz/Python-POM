import unittest
import testtools as testtools

import sys
import os
sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

from unittest import TestLoader, TestSuite, TextTestRunner
from Test.Scripts.test_A_Home_Page import Onet_HomePage
from Test.Scripts.test_B_Mail_Page import Onet_MailPage
from Test.Scripts.test_C_Mail_Page_Login_Valid import Onet_MailLoginPageValid
from Test.Scripts.test_D_Mail_Page_Login_Invalid import Onet_MailLoginPageInvalid


if __name__ == "__main__":
 
    
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(Onet_HomePage),
        test_loader.loadTestsFromTestCase(Onet_MailPage),
        test_loader.loadTestsFromTestCase(Onet_MailLoginPageValid),
        test_loader.loadTestsFromTestCase(Onet_MailLoginPageInvalid),
        ))
 
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
    # Refer https://testtools.readthedocs.io/en/latest/api.html for more information
    parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    parallel_suite.run(testtools.StreamResult())