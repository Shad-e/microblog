"""
Fixtures for tests
"""
# pylint: disable=redefined-outer-name
import os
import pytest
from app import create_app, db
from app.config import TestConfig

os.environ['SQLALCHEMY_SILENCE_UBER_WARNING'] = '1' # FIX ?? 


@pytest.fixture(scope='function')
def test_app():
    """
    Create Flask app fixture
    """
    app = create_app(TestConfig)
    app_context = app.app_context()
    app_context.push()
    db.create_all()

    yield app

    db.session.remove()
    db.drop_all()
    app_context.pop()


@pytest.fixture(scope="function")
def client(test_app):
    """
    Create client for app
    """
    return test_app.test_client()
