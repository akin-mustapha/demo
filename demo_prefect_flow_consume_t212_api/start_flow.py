import logging
from prefect import flow
from dotenv import load_dotenv
from datetime import timedelta

from tasks.save_to_db import save_to_db
from tasks.fetch_account_cash import fetch_account_cash

load_dotenv(".env")

logging.basicConfig(level=logging.INFO, filename="./logs/info.log", format="%(asctime)s - %(levelname)s - %(message)s")

logging.basicConfig(level=logging.ERROR, filename="./logs/error.log", format="%(asctime)s - %(levelname)s - %(message)s")


@flow
def my_flow():
    logging.info("Starting the flow to fetch account cash")
    # task 1: fetch account cash
    data = fetch_account_cash()
    if data:
        # task 2: save to db
        save_to_db(data)

cron="1 * * * *"
if __name__ == "__main__":
    my_flow.serve(
        name="trading212_flow", interval=timedelta(seconds=180))  # Runs every 60 seconds