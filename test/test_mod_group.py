from model.group import Group
from login import Login

def test_add_group(app):
    app.session.make_login(Login(username="admin", password="secret"))
    app.group.modify(Group(name="TestX", header="TestY", footer="TestW"))
    app.session.logout()
