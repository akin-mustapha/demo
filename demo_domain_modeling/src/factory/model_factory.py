from ..model import model
from inspect import isclass, ismodule


class ModelFactory:
  def __init__(self):
    self.registry = {}
  
  def load_models(self):
    for m in model:
      self.registry[m.__name__.lower()] = m

  def get_model(self, model_name: str):
    return self.registry.get(model_name.lower())