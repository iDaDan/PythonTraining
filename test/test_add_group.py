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
        app.session.make_login(Login(username="admin", password="secret"))
        app.group.open_group_page()
        app.group.create(Group(name="Test", header="Test1", footer="Test2"))
        app.group.return_group_page()
        app.session.logout()

def test_add_empty_group(app):
        app.session.make_login(Login(username="admin", password="secret"))
        app.group.open_group_page()
        app.group.create(Group(name="", header="", footer=""))
        app.group.return_group_page ()
        app.session.logout()

