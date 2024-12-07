# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class test_name_user(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        
        
    def test_add_user(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element("name","user").click()
        wd.find_element("name","user").clear()
        wd.find_element("name","user").send_keys("admin")
        wd.find_element("name","pass").clear()
        wd.find_element("name","pass").send_keys("secret")
        wd.find_element("xpath","//input[@value='Login']").click()
        #add to separate method/class
        wd.find_element("link text","add new").click()
        wd.find_element("name","firstname").click()
        wd.find_element("name","firstname").clear()
        wd.find_element("name","firstname").send_keys("Tor")
        wd.find_element("name","middlename").click()
        wd.find_element("name","middlename").clear()
        wd.find_element("name","middlename").send_keys("Ivanov")
        wd.find_element("name","lastname").click()
        wd.find_element("name","lastname").clear()
        wd.find_element("name","lastname").send_keys("Odinovich")
        wd.find_element("name","nickname").click()
        wd.find_element("name","nickname").clear()
        wd.find_element("name","nickname").send_keys("GodOfThunder")
        wd.find_element("name","theform").click()
        wd.find_element("name","nickname").click()
        wd.find_element("name","nickname").click()
        wd.find_element("name","title").click()
        wd.find_element("name","title").clear()
        wd.find_element("name","title").send_keys("What is Title")
        wd.find_element("name","company").click()
        wd.find_element("name","company").clear()
        wd.find_element("name","company").send_keys("Asgard")
        wd.find_element("name","address").click()
        wd.find_element("name","address").clear()
        wd.find_element("name","address").send_keys("Still Asgard")
        wd.find_element("name","home").click()
        wd.find_element("name","home").clear()
        wd.find_element("name","home").send_keys("Bifrust")
        wd.find_element("name","mobile").clear()
        wd.find_element("name","mobile").send_keys("Sacrifice")
        wd.find_element("name","work").click()
        wd.find_element("name","work").clear()
        wd.find_element("name","work").send_keys("Hammer Management")
        wd.find_element("name","fax").click()
        wd.find_element("name","fax").clear()
        wd.find_element("name","fax").send_keys("Axe")
        wd.find_element("name","email").click()
        wd.find_element("name","email").clear()
        wd.find_element("name","email").send_keys("thor@asgard.ru")
        wd.find_element("name","homepage").click()
        wd.find_element("name","homepage").clear()
        wd.find_element("name","homepage").send_keys("thor.asgard.ru")
        wd.find_element("name","bday").click()
        Select(wd.find_element("name","bday")).select_by_visible_text("16")
        wd.find_element("name","bmonth").click()
        Select(wd.find_element("name","bmonth")).select_by_visible_text("October")
        wd.find_element("name","byear").click()
        wd.find_element("name","byear").clear()
        wd.find_element("name","byear").send_keys("1000")
        wd.find_element("name","aday").click()
        Select(wd.find_element("name","aday")).select_by_visible_text("17")
        wd.find_element("name","amonth").click()
        Select(wd.find_element("name","amonth")).select_by_visible_text("November")
        wd.find_element("name","ayear").click()
        wd.find_element("name","ayear").clear()
        wd.find_element("name","ayear").send_keys("1001")
        wd.find_element("xpath","//div[@id='content']/form/input[20]").click()
        wd.find_element("link text","home").click()

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
