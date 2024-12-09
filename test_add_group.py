# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import Group
from login import Login
from application_fixture import Application
import unittest
import pytest

class test_name_group(unittest.TestCase):

    @pytest.fixture()
    def app(request):
        fixture = Application()
        request.addfinalyser(fixture.destroy)
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

