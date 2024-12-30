from login import Login

def test_delete_first_user(app):
    app.session.make_login(Login(username="admin", password="secret"))
    app.open_home_page()
    app.user.delete_user()
    app.session.logout()