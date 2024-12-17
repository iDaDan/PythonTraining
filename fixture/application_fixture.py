from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element("link text", "Logout").click()

    def return_group_page(self):
        wd = self.wd
        wd.find_element("link text", "group page").click()

    def create_group(self, group):
        wd = self.wd
        wd.find_element("name", "new").click()
        # fill group firm
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys(group.name)
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys(group.header)
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element("name", "submit").click()

    def open_group_page(self):
        wd = self.wd
        wd.find_element("link text", "groups").click()

    def make_login(self, login):
        wd = self.wd
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys(login.username)
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys(login.password)
        wd.find_element("xpath", "//input[@value='Login']").click()

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

    def create_user(self, user):
        wd = self.wd
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

    def destroy(self):
        self.wd.quit()