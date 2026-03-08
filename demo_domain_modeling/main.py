import json
import pathlib
import os
import pandas as pd
import logging

from src.factory import ModelFactory
from src.model.apartment_block import ApartmentBlock
from src.model.apartment import Apartment
from src.model.employee import Employee
from src.model.tenant import Tenant


logging.basicConfig(level=logging.INFO)
data_path = pathlib.Path(os.path.dirname(__file__)) / 'data'

data_registry = {
    "apartmentblock": 'apartment_block.csv',
    "apartment": 'apartment.csv',
    "employee": 'employee.csv',
    "tenant": 'tenant.csv'
}

def load_data(file_path: str, model):
    logging.info(f"Loading data from {file_path} into model {model.__name__}")
    objs = []

    data = pd.read_csv(file_path).to_dict(orient='records')
    for item in data:
        obj = model(**item)
        objs.append(obj)

    return objs

if __name__ == "__main__":
    print("This module contains data models for the apartment management system.")

    model_factory = ModelFactory()
    model_factory.load_models()


    for model, path in data_registry.items():
        entities = load_data(f"{data_path}/{path}", model_factory.get_model(model))

        logging.info(f"Loaded {len(entities)} entities of type {model_factory.get_model(model).__name__}")