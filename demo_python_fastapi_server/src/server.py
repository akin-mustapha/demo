from fastapi import FastAPI # SERVER
from fastapi import BackgroundTasks # BACKGROUND TASKS
import logging
import time
from apscheduler.schedulers.background import BackgroundScheduler # Periodic TASKS

logging.basicConfig(level=logging.INFO)
app = FastAPI()

schedular = BackgroundScheduler()
schedular.start()

def periodic_task():
  logging.info("Periodic task executed")

schedular.add_job(periodic_task, 'interval', seconds=30)

@app.get("/")
def home():
  return {"message": "Server is alive"}

@app.get("/hello")
def hello_world():
  return {"message": "Hello, World!"}

@app.get("/health")
def health_check():
  return {"message": "Server is healthy"}

@app.get("/greet/{name}")
def greet(name: str):
  return {"message": f"Hello, {name}!"}

tasks = {}
@app.post("/add_task/{task_name}")
def add_teask(task_name):
  id = len(tasks) + 1
  tasks[id] = {"name": task_name, "done": False}
  logging.info(f"Task added: {task_name} with id {id}")
  return {"id": id, "task": tasks[id]}

@app.get("/list_tasks")
def list_tasks():
  return tasks

def background_task(task_name: str):
  time.sleep(10)
  logging.info(f"Task {task_name} completed")

@app.post("/run_task/{task_id}")
def run_task(task_id: int, background_tasks: BackgroundTasks):
  task = tasks.get(task_id)
  if not task:
    return {"error": "Task not found"}
  logging.info(f"Running task {task_id} in the background")
  background_tasks.add_task(background_task, task["name"])
  return {"message": f"Task {task_id} is running in the background"}