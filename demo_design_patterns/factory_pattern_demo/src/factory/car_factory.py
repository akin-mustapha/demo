from ..models import models
from inspect import isclass, ismodule

class CarFactory:
  def __init__(self):
    self.registry = {}

  def load(self):
    for model in models:
      self.registry.update({model.__name__.lower(): model})

  def get_car(self, model_name: str):
    return self.registry.get(model_name.lower(), self.registry['null'])


if __name__ == "__main__":
  factory = CarFactory()

  factory.load()

  car = factory.get_car('Audi')()
  car.start()
  car.refuel()
  car.off()


  car = factory.get_car('Toyota')()
  car.start()
  car.refuel()
  car.off()