import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


# ✅ Test homepage loads
def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200


# ✅ Test valid search (use a team you KNOW exists)
def test_valid_search(client):
    response = client.get('/search?team=Arsenal')
    assert response.status_code == 200


# ✅ Test invalid search (should return 404)
def test_invalid_search(client):
    response = client.get('/search?team=xyz123')
    assert response.status_code == 404


# ✅ Test random invalid URL
def test_404_page(client):
    response = client.get('/randompage')
    assert response.status_code == 404