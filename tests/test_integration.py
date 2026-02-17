from fastapi.testclient import TestClient
from app.main import app, tasks

client = TestClient(app)

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) == len(tasks)
    
def test_get_task():
    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    
def test_get_task_not_found():
    response = client.get("/tasks/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}
    
def test_create_task():
    new_task = {"title": "New Task", "description": "New Desc"}
    response = client.post("/tasks", json=new_task)
    
    assert response.status_code == 200
    data = response.json()
    
    assert "id" in data
    assert data["title"] == "New Task"
    assert data["description"] == "New Desc"
    assert data["completed"] is False
    
def test_complete_task():
    response = client.put("/tasks/1/complete")
    assert response.status_code == 200
    assert response.json()["completed"] is True
    
def test_delete_task():
    response = client.delete("/tasks/6")
    assert response.status_code == 200
    assert response.json() == {"message": "Task deleted"}
    
    response = client.get("/tasks/6")
    assert response.status_code == 404