from login import Login
import pytest

@pytest.fixture()
def test_delete_first_group(app):
    app.session.make_login(Login(username="admin", password="secret"))
    app.group.delete_first_group()
    app.session.logout()

