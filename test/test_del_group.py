from login import Login

def test_delete_first_group(app):
    app.session.make_login(Login(username="admin", password="secret"))
    app.group.delete_first_group()
    app.session.logout()

