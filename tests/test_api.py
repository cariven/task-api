from fastapi.testclient import TestClient
from src.main import app
from src.database import tasks

client = TestClient(app)

def setup_function():
    tasks.clear()

def test_create_task_api():
    res = client.post("/tasks", params={"title": "API Task"})
    assert res.status_code == 200

def test_get_tasks_api():
    client.post("/tasks", params={"title": "A"})
    res = client.get("/tasks")
    assert len(res.json()) == 1

def test_update_task_api():
    client.post("/tasks", params={"title": "A"})
    res = client.put("/tasks/1", params={"status": "done"})
    assert res.json()["status"] == "done"

def test_invalid_status_api():
    client.post("/tasks", params={"title": "A"})
    res = client.put("/tasks/1", params={"status": "invalid"})
    assert res.status_code == 400

def test_task_not_found_api():
    res = client.put("/tasks/99", params={"status": "done"})
    assert res.status_code == 400