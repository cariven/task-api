from fastapi import FastAPI, HTTPException
from src.service import create_task, get_tasks, update_task

app = FastAPI()

@app.post("/tasks")
def add_task(title: str):
    try:
        return create_task(title)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/tasks")
def read_tasks():
    return get_tasks()

@app.put("/tasks/{task_id}")
def edit_task(task_id: int, status: str):
    try:
        return update_task(task_id, status)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))