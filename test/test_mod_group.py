from model.group import Group
from login import Login

def test_mod_first_group(app):
    app.session.make_login(Login(username="admin", password="secret"))
    app.group.modify_first_group(Group(name="TestX", header="TestY", footer="TestW"))
    app.session.logout()

def test_mod_name_first_group(app):
    app.session.make_login(Login(username="admin", password="secret"))
    app.group.modify_first_group(Group(name="NaMeNaMe"))
    app.session.logout()