__author__ = 'Ben'

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from Pages.loginPage import LoginPage
from Pages.dashboardPage import DashboardPage
import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "", ""))


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # Login to dashboard with valid credentials
    def test_01_valid_login(self):
        login = LoginPage(self.driver)
        login.valid_login_with_credentials("", "")
        dashboard = DashboardPage(self.driver)
        dashboard.screen_loaded()
        dashboard.log_out()

    # Attempt to login to dashboard with invalid credentials
    def test_02_login_with_invalid_credentials(self):
        login = LoginPage(self.driver)
        self.wait = WebDriverWait(self.driver, 10)
        login.valid_login_with_credentials("admin", "test")
        error_msg = self.wait.until(
            presence_of_element_located((By.XPATH, "//div[contains(@class,'login-error-container')]/p")))
        time.sleep(2)
        self.assertEqual(error_msg.text, "We didn't recognize that email and/or password. Need help?",
                         "Login Error message is incorrect")
        print("Login error message is visible")

    # Attempt to login to dashboard with an invalid username and valid password
    def test_03_login_with_empty_username(self):
        login = LoginPage(self.driver)
        self.wait = WebDriverWait(self.driver, 10)
        login.valid_login_with_credentials("", "")
        error_msg = self.wait.until(
            presence_of_element_located((By.XPATH, "//div[contains(@class,'login-error-container')]/p")))
        time.sleep(2)
        self.assertEqual(error_msg.text, "We didn't recognize that email and/or password. Need help?",
                         "Login Error message is incorrect")
        print("Login error message is visible")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test Completed")


if __name__ == '__main__':
    unittest.main()

