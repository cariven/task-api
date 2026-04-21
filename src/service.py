from src.database import tasks
from src.models import Task

def create_task(title):
    if not title:
        raise ValueError("Title cannot be empty")

    task = Task(id=len(tasks)+1, title=title)
    tasks.append(task)
    return task

def get_tasks():
    return tasks

def update_task(task_id, status):
    for task in tasks:
        if task.id == task_id:
            if status not in ["pending", "done"]:
                raise ValueError("Invalid status")
            task.status = status
            return task
    raise ValueError("Task not found")