import pytest
from fixture.application_fixture import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

# для создания, удаления и модификации групп и контактов