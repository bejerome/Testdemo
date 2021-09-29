__author__ = 'Ben'
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.username_username_id = "email"
        self.username_password_id = "password"
        self.login_button_id = "logIn"
        self.remember_me_checkbox_id = "remember-me"
        self.forget_password_link_id = "forgot-password-link"
        self.login_with_org_id = "logInWithOrganization"
        self.url = "https://www.hudl.com/login"

    def open_url(self):
        self.driver.get(self.url)

    def enter_username(self, user_name):
        self.driver.find_element_by_id(self.username_username_id).clear()
        print("clear username")
        self.driver.find_element_by_id(self.username_username_id).send_keys(user_name)
        print("enter username")

    def enter_password(self, password):
        self.driver.find_element_by_id(self.username_password_id).clear()
        print("clear password")
        self.driver.find_element_by_id(self.username_password_id).send_keys(password)
        print("enter password")

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()
        print("clicked on login button")

    def valid_login_with_credentials(self, username, password):
        self.open_url()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def validate_login_error(self):
        error_msg = self.wait.until(
            presence_of_element_located((By.XPATH, "//div[contains(@class,'login-error-container')]/p")))


