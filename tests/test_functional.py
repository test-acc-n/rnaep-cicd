from fastapi.testclient import TestClient
from app.main import app, tasks

client = TestClient(app)

def test_user_can_create_complete_and_delete_task():
    create_response = client.post("/tasks", json={
        "title": "Workout",
        "description": "Gym session"
    })
    assert create_response.status_code == 200
    assert create_response.json()["title"] == "Workout"
    assert create_response.json()["description"] == "Gym session"
    task_id = create_response.json()["id"]

    complete_response = client.put(f"/tasks/{task_id}/complete")
    assert complete_response.status_code == 200

    get_response1 = client.get(f"/tasks/{task_id}")
    assert get_response1.json()["completed"] is True
    
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200

    get_response2 = client.get(f"/tasks/{task_id}")
    assert get_response2.status_code == 404
