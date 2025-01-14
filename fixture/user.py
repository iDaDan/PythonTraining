from selenium.webdriver.support.ui import Select
class UserHelper:

    def __init__(self, app):
        self.app = app

    def create_user(self, user):
        wd = self.app.wd
        wd.find_element("link text", "add new").click()
        self.fill_user_info(user)
        wd.find_element("xpath", "//div[@id='content']/form/input[20]").click()

    def delete_user(self):
        wd = self.app.wd
        wd.find_element("name", "selected[]").click()
        wd.find_element("xpath", '//*[@id="content"]/form[2]/div[2]/input').click()

    def modify_user(self, user):
        wd = self.app.wd
        wd.find_element("name", "selected[]").click()
        wd.find_element('xpath','//*[@id="maintable"]/tbody/tr[2]/td[8]/a/img').click()
        self.fill_user_info(user)
        wd.find_element("name", "update").click()

    def fill_user_info(self, user):
        wd = self.app.wd
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