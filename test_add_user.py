# -*- coding: utf-8 -*-
from login import Login
from user import User
from app_user_fixture import UserApp
import pytest


@pytest.fixture()
def app(request):
    fixture = UserApp()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.open_home_page()
    app.make_login(Login(username="admin", password="secret"))
    # add to separate method/class
    app.create_user(User(firstname="Thor", middlename="Ivanov", lastname="Odinovich", nickname="GodOfThunder",
                         title="What is Title", company="Asgard", address="Still Asgard", home="Bifrust",
                         mobile="Sacrifice", work="Hammer Management", fax="Axe", email="thor@asgard.ru",
                         homepage="thor.asgard.ru", bday="5", bmonth="October", byear="1000",
                         aday="6", amonth="November", ayear="1001"))
    app.return_home_page()
    app.logout()


def test_add_empty_user(app):
    app.open_home_page()
    app.make_login(Login(username="admin", password="secret"))
    # add to separate method/class
    app.create_user(User(firstname="", middlename="", lastname="", nickname="",
                         title="", company="", address="", home="",
                         mobile="", work="", fax="", email="",
                         homepage="", bday="5", bmonth="October", byear="1000",
                         aday="6", amonth="November", ayear="1001"))
    app.return_home_page()
    app.logout()
