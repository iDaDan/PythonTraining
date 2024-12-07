# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from login import Login
from user import User
import unittest


class test_name_user(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def test_add_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.make_login(wd, Login(username="admin", password="secret"))
        # add to separate method/class
        self.create_user(wd, User(firstname = "Thor", middlename = "Ivanov", lastname = "Odinovich", nickname = "GodOfThunder",
                                  title = "What is Title", company = "Asgard", address = "Still Asgard", home = "Bifrust",
                                  mobile = "Sacrifice", work = "Hammer Management", fax = "Axe", email = "thor@asgard.ru",
                                  homepage = "thor.asgard.ru", bday = "5", bmonth = "October", byear = "1000",
                                  aday = "6", amonth = "November", ayear = "1001"))
        self.return_home_page(wd)
        self.logout(wd)

    def test_add_empty_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.make_login(wd, Login(username="admin", password="secret"))
        # add to separate method/class
        self.create_user(wd, User(firstname = "", middlename = "", lastname = "", nickname = "",
                                  title = "", company = "", address = "", home = "",
                                  mobile = "", work = "", fax = "", email = "",
                                  homepage = "", bday = "5", bmonth = "October", byear = "1000",
                                  aday = "6", amonth = "November", ayear = "1001"))
        self.return_home_page(wd)
        self.logout(wd)

    def return_home_page(self, wd):
        wd.find_element("link text", "home").click()

    # will be debugged later
    def fill_element_by_name(self, wd, indicator, text):
        self.text = text
        self.indicator = indicator
        wd.find_element("name", indicator).click()
        wd.find_element("name", indicator).clear()
        wd.find_element("name", indicator).send_keys(text)

    def create_user(self, wd, user):
        wd.find_element("link text", "add new").click()
        # fill_element_by_name(self, wd, "firstname", "Thor")
        wd.find_element("name", "firstname").click()
        wd.find_element("name", "firstname").clear()
        wd.find_element("name", "firstname").send_keys(user.firstname)
        wd.find_element("name", "middlename").click()
        wd.find_element("name", "middlename").clear()
        wd.find_element("name", "middlename").send_keys(user.middlename)
        wd.find_element("name", "lastname").click()
        wd.find_element("name", "lastname").clear()
        wd.find_element("name", "lastname").send_keys(user.lastname)
        wd.find_element("name", "nickname").click()
        wd.find_element("name", "nickname").clear()
        wd.find_element("name", "nickname").send_keys(user.nickname)
        wd.find_element("name", "title").click()
        wd.find_element("name", "title").clear()
        wd.find_element("name", "title").send_keys(user.title)
        wd.find_element("name", "company").click()
        wd.find_element("name", "company").clear()
        wd.find_element("name", "company").send_keys(user.company)
        wd.find_element("name", "address").click()
        wd.find_element("name", "address").clear()
        wd.find_element("name", "address").send_keys(user.address)
        wd.find_element("name", "home").click()
        wd.find_element("name", "home").clear()
        wd.find_element("name", "home").send_keys(user.home)
        wd.find_element("name", "mobile").clear()
        wd.find_element("name", "mobile").send_keys(user.mobile)
        wd.find_element("name", "work").click()
        wd.find_element("name", "work").clear()
        wd.find_element("name", "work").send_keys(user.work)
        wd.find_element("name", "fax").click()
        wd.find_element("name", "fax").clear()
        wd.find_element("name", "fax").send_keys(user.fax)
        wd.find_element("name", "email").click()
        wd.find_element("name", "email").clear()
        wd.find_element("name", "email").send_keys(user.email)
        wd.find_element("name", "homepage").click()
        wd.find_element("name", "homepage").clear()
        wd.find_element("name", "homepage").send_keys(user.homepage)
        wd.find_element("name", "bday").click()
        Select(wd.find_element("name", "bday")).select_by_visible_text(user.bday)
        wd.find_element("name", "bmonth").click()
        Select(wd.find_element("name", "bmonth")).select_by_visible_text(user.bmonth)
        wd.find_element("name", "byear").click()
        wd.find_element("name", "byear").clear()
        wd.find_element("name", "byear").send_keys(user.byear)
        wd.find_element("name", "aday").click()
        Select(wd.find_element("name", "aday")).select_by_visible_text(user.aday)
        wd.find_element("name", "amonth").click()
        Select(wd.find_element("name", "amonth")).select_by_visible_text(user.amonth)
        wd.find_element("name", "ayear").click()
        wd.find_element("name", "ayear").clear()
        wd.find_element("name", "ayear").send_keys(user.ayear)
        wd.find_element("xpath", "//div[@id='content']/form/input[20]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def make_login(self, wd, login):
        wd.find_element("name", "user").click()
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys(login.username)
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys(login.password)
        wd.find_element("xpath", "//input[@value='Login']").click()

    def logout(self, wd):
        wd.find_element("link text", "Logout").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
