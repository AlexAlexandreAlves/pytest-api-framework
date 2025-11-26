import pytest
from src.api_endpoints import Endpoints
from tests.data.activities import ACTIVITIES_POST_DATA, ACTIVITIES_BY_ID_DATA


@pytest.mark.parametrize("activity", ACTIVITIES_BY_ID_DATA)
def test_get_activity_by_id(api_client, activity):
    response = api_client.get(Endpoints.ACTIVITIES_BY_ID, id=activity["id"])

    assert response.status_code == 200

    body = response.json()
    assert body.get("id") == activity["id"]
    assert body.get("title") == activity["title"]


def test_get_activities(api_client):
    response = api_client.get(Endpoints.ACTIVITIES)

    assert response.status_code == 200

    body = response.json()
    assert isinstance(body, list)  # Verify if its a list
    assert len(body) == 30  # Verify the number of activities


@pytest.mark.parametrize("activity", ACTIVITIES_POST_DATA)
def test_create_activities(api_client, activity):
    response = api_client.post(Endpoints.ACTIVITIES, data=activity)
    body = response.json()

    assert response.status_code == 200

    assert body.get("title") == activity["title"]
    assert body.get("dueDate") == activity["dueDate"]
    assert body.get("completed") == activity["completed"]
