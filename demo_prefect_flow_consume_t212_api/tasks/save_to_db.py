from prefect import task
from database.database import save_to_db_session, start_database
import logging

logging.basicConfig(level=logging.INFO)

@task
def save_to_db(data: dict):
        engine = start_database()
        save_to_db_session(engine, data)

        logging.info("Data saved to database successfully")