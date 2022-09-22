from app import app
import pytest
import json, io, os

@pytest.fixture(scope='module')
def test_client():
    flask_app = app
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client

@pytest.fixture(autouse=True, scope='session')
def pytest_sessionstart():
    os.system("make clean")
    os.system("make")
