import pytest
from src.api_endpoints import Endpoints
from tests.data.activities import ACTIVITIES_DATA

def test_get_activities(api_client):
    response = api_client.get(Endpoints.ACTIVITIES)
    assert response.status_code == 200  
    
    body = response.json()
    assert isinstance(body, list)  # Verify if its a list
    assert len(body) == 30  # Verify the number of activities


@pytest.mark.parametrize("activity", ACTIVITIES_DATA)
def test_create_activities(api_client, activity):
    response = api_client.post(Endpoints.ACTIVITIES, data=activity)

    # save the response body
    body = response.json()
    # assertions
    assert response.status_code == 200
    assert body.get("title") == activity["title"]
    assert body.get("dueDate") == activity["dueDate"]
    assert body.get("completed") == activity["completed"]

