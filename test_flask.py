'''Test Case to ensure Flask is running'''
# import json
# import io
import os
import pytest
from app import app


@pytest.fixture(scope='module')
def test_client():
    '''Sets up client server'''
    flask_app = app
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client

@pytest.fixture(autouse=True, scope='session')
def pytest_sessionstart():
    '''Sets up compiler'''
    os.system("make clean")
    os.system("make")
    os.system("python -m flask run")

# def no_class(test_client):
