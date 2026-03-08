from sqlmodel import SQLModel, Field
from datetime import datetime


class Task(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  name: str
  description: str | None = None # default
  status: str = "pending" # default value
  created_at: datetime = Field(default_factory=datetime.utcnow)