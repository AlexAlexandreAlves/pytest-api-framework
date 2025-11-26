from src.api_endpoints import Endpoints


def test_get_activities(api_client):
    response = api_client.get(Endpoints.ACTIVITIES)
    assert response.status_code == 200  
    
    body = response.json()
    assert isinstance(body, list)  # Verify if its a list
    assert len(body) == 30  # Verify the number of activities


def test_create_activities(api_client):
    new_activity = {"title": "Jump",
                    "dueDate": "2024-12-31T23:59:59Z", "completed": True}
    response = api_client.post(Endpoints.ACTIVITIES, data=new_activity)

    # save the resonse body
    body = response.json()
    # assertions
    assert response.status_code == 200
    assert body.get("title") == "Jump"
    assert body.get("dueDate") == "2024-12-31T23:59:59Z"
    assert body.get("completed") is True
