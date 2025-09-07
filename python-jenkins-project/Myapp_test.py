from flask.testing import FlaskClient
import pytest
from Myapp import app, add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(8, 2) == 4
    assert divide(8, 0) == "Error: Division by zero"


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home_route(client: FlaskClient):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data