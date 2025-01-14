class SessionHelper:

    def __init__(self, app):
        self.app = app

    def make_login(self, login):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys(login.username)
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys(login.password)
        wd.find_element("xpath", "//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element("link text", "Logout").click()
