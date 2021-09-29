__author__ = 'Ben'
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_bar_class = "uni-form__input search-bar__input"
        self.tab_feed_text = "Feed"
        self.tab_trending_text = "Trending"
        self.tab_featured_text = "Featured"
        self.tab_your_team_text = "Teams"
        self.logout_dropdown_btn = "hui-globaluseritem__display-name"
        self.logout_btn = "webnav-usermenu-logout"
        # set the timeout to 10 seconds
        self.wait = WebDriverWait(self.driver, 10)

    def screen_loaded(self):
        elements = [self.tab_feed_text, self.tab_trending_text, self.tab_featured_text, self.tab_your_team_text]
        for x in elements:
            self.wait.until(presence_of_element_located((By.XPATH,  f'//*[contains(text(), {x})]')))
            print(f"{x} tab bar is visible")
        self.wait.until(presence_of_element_located((By.ID, "notifications-link")))
        print("dashboard page is loaded")

    def log_out(self):
        avatar = self.driver.find_element_by_class_name("uni-avatar__content-container")
        avatar.click()
        self.wait.until(presence_of_element_located((By.XPATH, '//*[@id="ssr-webnav"]/div/div[1]/nav[1]/div[4]/div[2]/div[2]/div[3]/a/span')))
        self.driver.find_element_by_xpath('//*[@id="ssr-webnav"]/div/div[1]/nav[1]/div[4]/div[2]/div[2]/div[3]/a/span').click()
        self.wait.until(presence_of_element_located((By.XPATH, "/html/body/div[2]/header/div[2]/ul/li[3]/a")))
