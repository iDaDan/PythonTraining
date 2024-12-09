from selenium import webdriver

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

    def destroy(self):
        self.wd.quit()