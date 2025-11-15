"""
Tests for the Flask API
"""
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    """Test health endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_db_check(client):
    """Test database check endpoint"""
    response = client.get('/db/check')
    assert response.status_code == 200
    assert response.json['status'] == 'ok'
    assert 'psycopg2_version' in response.json
