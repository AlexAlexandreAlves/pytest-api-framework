import pytest
from src.api_endpoints import Endpoints

def test_get_users(api_client):
    response = api_client.get(Endpoints.GROUPS)
    assert response.status_code == 200
    # assert isinstance(response.json(), list)  # Assumindo que a resposta é uma lista de usuários.

# def test_create_user(api_client):
#     new_user = {"name": "John Doe", "email": "john@example.com"}
#     response = api_client.post(Endpoints.USERS, data=new_user)
#     assert response.status_code == 201
#     assert response.json().get("name") == new_user["name"]