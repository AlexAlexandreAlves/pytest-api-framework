import pytest
from src.api_client import APIClient
    
@pytest.fixture(scope="module")
def api_client():
    client = APIClient(base_url="https://dogapi.dog/api/v2/")
    yield client