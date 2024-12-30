from model.user import User
from login import Login

def test_add_user(app):
    app.session.make_login(Login(username="admin", password="secret"))
    app.open_home_page()
    # add to separate method/class
    app.user.modify_user(User(firstname="XThor", middlename="XIvanov", lastname="XOdinovich", nickname="XGodOfThunder",
                              title="XWhat is Title", company="XAsgard", address="XStill Asgard", home="XBifrust",
                              mobile="XSacrifice", work="XHammer Management", fax="XAxe", email="Xthor@asgard.ru",
                              homepage="Xthor.asgard.ru", bday="7", bmonth="October", byear="1000",
                              aday="6", amonth="November", ayear="1011"))
    app.return_home_page()
    app.session.logout()
