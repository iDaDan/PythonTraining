# -*- coding: utf-8 -*-
from model.group import Group
from login import Login
from fixture.application_fixture import Application
import pytest

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
        app.open_home_page()
        app.make_login(Login(username="admin", password="secret"))
        app.open_group_page()
        app.create_group(Group(name="Test", header="Test1", footer="Test2"))
        app.return_group_page()
        app.logout()

def test_add_empty_group(app):
        app.open_home_page()
        app.make_login(Login(username="admin", password="secret"))
        app.open_group_page()
        app.create_group(Group(name="", header="", footer=""))
        app.return_group_page()
        app.logout()

