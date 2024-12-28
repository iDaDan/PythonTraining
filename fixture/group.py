class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_group_page(self):
        wd = self.app.wd
        wd.find_element("link text", "group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
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
        self.return_group_page()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element("link text", "groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        #select_first_group
        wd.find_element("name", "selected[]").click()
        #sibmit deletion
        wd.find_element("name", "delete").click()

    def modify(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element("name", "selected[]").click()
        wd.find_element("name", "edit").click()
        # fill group firm
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys(group.name)
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys(group.header)
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element("name", "update").click()
        self.return_group_page()