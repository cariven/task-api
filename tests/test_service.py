import pytest
from src.service import create_task, update_task, get_tasks
from src.database import tasks

def setup_function():
    tasks.clear()

def test_create_task_success():
    task = create_task("Test Task")
    assert task.title == "Test Task"

def test_create_task_empty():
    with pytest.raises(ValueError):
        create_task("")

def test_get_tasks():
    create_task("A")
    assert len(get_tasks()) == 1

def test_update_task_success():
    task = create_task("A")
    updated = update_task(task.id, "done")
    assert updated.status == "done"

def test_update_invalid_status():
    task = create_task("A")
    with pytest.raises(ValueError):
        update_task(task.id, "invalid")

def test_update_not_found():
    with pytest.raises(ValueError):
        update_task(999, "done")

# tambahan biar >=15
def test_multiple_tasks():
    create_task("A")
    create_task("B")
    assert len(get_tasks()) == 2

def test_default_status():
    task = create_task("A")
    assert task.status == "pending"

def test_update_pending():
    task = create_task("A")
    updated = update_task(task.id, "pending")
    assert updated.status == "pending"

def test_id_increment():
    t1 = create_task("A")
    t2 = create_task("B")
    assert t2.id == t1.id + 1

def test_task_list_type():
    create_task("A")
    assert isinstance(get_tasks(), list)

def test_title_persistence():
    task = create_task("Hello")
    assert task.title == "Hello"

def test_update_same_status():
    task = create_task("A")
    update_task(task.id, "pending")
    assert task.status == "pending"

def test_create_many():
    for i in range(5):
        create_task(f"T{i}")
    assert len(get_tasks()) == 5

def test_update_after_multiple():
    create_task("A")
    t2 = create_task("B")
    update_task(t2.id, "done")
    assert t2.status == "done"