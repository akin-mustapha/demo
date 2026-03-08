from sqlmodel import SQLModel, Field
from datetime import datetime

class Trading212AccountCash(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  free: float
  total: float
  ppl: float
  result: float
  invested: float
  pieCash: float
  blocked: float
  fetched_at: datetime = Field(default_factory=datetime.utcnow)
