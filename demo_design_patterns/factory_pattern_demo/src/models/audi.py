from ..interface.car_interface import CarInterface


class Audi(CarInterface):
  def __init__(self):
    super().__init__()


  def model_name(self):
    return 'Audi'

  def start(self):
    print(f"Starting {self.model_name()}")

  def refuel(self, liter):
    print(f"Refueling {self.model_name()}, {liter}")

  def stop(self):
    print(f"Turning off {self.model_name()}")


if __name__ == "__main__":
  car = Audi()

  car.start()
  car.refuel(3.5)
  car.stop()