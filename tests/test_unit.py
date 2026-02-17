import pytest
from pydantic import ValidationError
from app.main import get_next_id
from app.models import TaskCreate, Task

def test_get_next_id():
    assert get_next_id(0) == 1
    assert get_next_id(2) == 3
    assert get_next_id(10) == 11
    
def test_taskcreate_fields():
    task = TaskCreate(title="Test", description="Desc", completed=True)
    assert task.title == "Test"
    assert task.description == "Desc"
    assert task.completed is True
    
def test_taskcreate_invalid_type():
    with pytest.raises(ValidationError):
        TaskCreate(title="Test", description=123)

def test_taskcreate_defaults():
    task = TaskCreate(title="Test", description="Desc")
    assert task.completed is False
    
def test_task_inheritance():
    task_create = TaskCreate(title="Test", description="Desc")
    task = Task(id=1, **task_create.model_dump())
    
    assert task.id == 1
    assert task.title == "Test"
    assert task.description == "Desc"
    assert task.completed is False
