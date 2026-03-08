from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
import logging
from database import init_db, engine
from sqlmodel import Session
from models import Task
import json

logging.basicConfig(level=logging.INFO, filename='server.log',)
logging.basicConfig(level=logging.ERROR, filename='error.log',)

@asynccontextmanager
async def lifespan(app: FastAPI):
  logging.info("Server is starting up...")
  logging.info("Initializing the database...")
  init_db()
  
  yield
  engine.dispose()
  logging.info("Server is shutting down...")

app = FastAPI(lifespan=lifespan)

# endpoints
@app.get('/health')
def health_check():
  logging.info("Health check performed")
  return {"status": "healthy"}


# endpoint to add task
@app.post('/task')
def create_task(task: Task):
  logging.info(f"Creating task")
  with Session(engine) as session:
    session.add(task)
    session.commit()
    session.refresh(task)
  return task


# endpoint to list all tasks
@app.get('/tasks')
def list_tasks():
  logging.info("Listing all tasks")
  with Session(engine) as session:
    tasks = session.query(Task).all()
  return tasks


# endpoint to get a specific task
@app.get('/task/{task_id}')
def get_task(task_id: int):
  logging.info(f"Fetching task with id {task_id}")
  with Session(engine) as session:
    task = session.get(Task, task_id)
    if not task:
      logging.error(f"Task with id {task_id} not found")
      raise HTTPException(status_code=404, detail="Task not found")
  return task

# endpoint to update a task by id 
@app.put("/task/{task_id}")
def update_task(task_id: int, updated_task: Task):
  logging.info(f"Updating task with id {task_id}")
  with Session(engine) as session:
    task = session.get(Task, task_id)
    
    if not task:
      logging.error(f"Task with id {task_id} not found")
      raise HTTPException(status_code=404, detail="Task not found")
    
    for key, value in updated_task.dict(exclude_unset=True).items():
      setattr(task, key, value)
    session.add(task)
    session.commit()
    session.refresh(task)
  return task



# endpoint to delete a task by id
@app.delete("/task/{task_id}")
def delete_task(task_id: int):
  logging.info(f"Deleting task with id {task_id}")
  with Session(engine) as session:
    task = session.get(Task, task_id)
    if not task:
      logging.error(f"Task with id {task_id} not found")
      raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
  return {"detail": "Task deleted successfully"}