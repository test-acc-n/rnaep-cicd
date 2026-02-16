from fastapi import FastAPI
from app.models import Task, TaskCreate
from typing import List

app = FastAPI()

tasks: List[Task] = [
    Task(id=1, title="Task 1", description="Description 1", completed=False),
    Task(id=2, title="Task 2", description="Description 2", completed=True),
    Task(id=3, title="Task 3", description="Description 3", completed=False),
    Task(id=4, title="Task 4", description="Description 4", completed=True),
    Task(id=5, title="Task 5", description="Description 5", completed=False),
    Task(id=6, title="Task 6", description="Description 6", completed=True)
]

current_id = len(tasks)



@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    return {"error": "Task not found"}

@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    global current_id
    current_id += 1

    new_task = Task(id=current_id, **task.model_dump())
    tasks.append(new_task)

    return new_task

@app.put("/tasks/{task_id}/complete", response_model=Task)
def complete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            return task
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    return {"error": "Task not found"}