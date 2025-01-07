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
        self.fill_group_info(group)
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
        self.select_first_group()
        #sibmit deletion
        wd.find_element("name", "delete").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        #open modification form
        wd.find_element("name", "edit").click()
        # fill group firm
        self.fill_group_info(new_group_data)
        # submit group modification
        wd.find_element("name", "update").click()
        self.return_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element("name", "selected[]").click()

    def fill_group_info(self, group):
        wd = self.app.wd
        self.insert_group_info("group_name", group.name)
        self.insert_group_info("group_header", group.header)
        self.insert_group_info("group_footer", group.footer)

    def insert_group_info(self, find_name, info_text):
        wd = self.app.wd
        if info_text is not None:
            wd.find_element("name", find_name).click()
            wd.find_element("name", find_name).clear()
            wd.find_element("name", find_name).send_keys(info_text)
        else:
            pass
