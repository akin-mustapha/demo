import yaml

from .src.factory.car_factory import CarFactory

if __name__ == "__main__":
  with open("factory_pattern_demo/config.yaml") as f:
    config = yaml.safe_load(f)

  
  factory = CarFactory()
  
  factory.load()

  settings = config.get("settings", {})
  model = settings.get("car_model", '')
  refuel_size = settings.get("refuel_size", 0.0)

  car = factory.get_car(model)()

  car.start()
  car.refuel(refuel_size)
  car.stop()