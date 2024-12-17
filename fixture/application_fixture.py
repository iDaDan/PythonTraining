from selenium import webdriver

from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.user import UserHelper
class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def return_home_page(self):
        wd = self.wd
        wd.find_element("link text", "home").click()

    # will be debugged later
    def fill_element_by_name(self, indicator, text):
        wd = self.wd
        self.text = text
        self.indicator = indicator
        wd.find_element("name", indicator).click()
        wd.find_element("name", indicator).clear()
        wd.find_element("name", indicator).send_keys(text)

    def destroy(self):
        self.wd.quit()