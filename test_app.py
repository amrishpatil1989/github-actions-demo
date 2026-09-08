import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'ok'


def test_square(client):
    response = client.get('/square/5')
    assert response.get_json()['result'] == 25


def test_greet(client):
    response = client.get('/greet/Alice')
    assert response.get_json()['message'] == 'Hello, Alice!'