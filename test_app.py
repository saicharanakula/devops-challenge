import pytest
from app import app, items

@pytest.fixture(autouse=True)
def clear_items():
    # Clear the items list before each test
    items.clear()

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_items(client):
    response = client.get('/items')
    assert response.status_code == 200
    assert response.json == []

def test_create_item(client):
    response = client.post('/items', json={"name": "Item 1"})
    assert response.status_code == 201
    assert response.json == {"name": "Item 1"}
    assert items == [{"name": "Item 1"}]

def test_update_item(client):
    client.post('/items', json={"name": "Item 1"})
    response = client.put('/items/0', json={"name": "Updated Item"})
    assert response.status_code == 200
    assert response.json == {"name": "Updated Item"}
    assert items == [{"name": "Updated Item"}]

def test_delete_item(client):
    client.post('/items', json={"name": "Item 1"})
    response = client.delete('/items/0')
    assert response.status_code == 204
    assert items == []
