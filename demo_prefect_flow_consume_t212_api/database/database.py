
from sqlmodel import SQLModel, create_engine, Session
from database.model.model import Trading212AccountCash


def start_database():

    engine = create_engine("sqlite:///trading212.db")

    SQLModel.metadata.create_all(engine)

    return engine


def save_to_db_session(engine, data):

    with Session(engine) as session:
        account_cash = Trading212AccountCash(
            free=data.get("free", 0.0),
            total=data.get("total", 0.0),
            ppl=data.get("ppl", 0.0),
            result=data.get("result", 0.0),
            invested=data.get("invested", 0.0),
            pieCash=data.get("pieCash", 0.0),
            blocked=data.get("blocked", 0.0)
        )
        session.add(account_cash)
        session.commit()


    return Session(engine)