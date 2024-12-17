class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_group_page(self):
        wd = self.app.wd
        wd.find_element("link text", "group page").click()

    def create(self, group):
        wd = self.app.wd
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
        wd = self.app.wd
        wd.find_element("link text", "groups").click()
