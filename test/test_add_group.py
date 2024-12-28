# -*- coding: utf-8 -*-
from model.group import Group
from login import Login


def test_add_group(app):
    app.session.make_login(Login(username="admin", password="secret"))
    app.group.create(Group(name="Testiiii", header="Test1", footer="Test2"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.make_login(Login(username="admin", password="secret"))
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
