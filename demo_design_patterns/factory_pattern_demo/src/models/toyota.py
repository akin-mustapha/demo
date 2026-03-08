from ..interface.car_interface import CarInterface


class Toyota(CarInterface):
  def __init__(self):
    super().__init__()


  def model_name(self):
    return 'Toyota'

  def start(self):
    print(f"Starting a {self.model_name()}")

  def stop(self):
    print(f"Putting off {self.model_name()}")

  def refuel(self, liter):
    print(f"Refueling {self.model_name()}")



if __name__ == "__main__":
  car = Toyota()

  car.start()
  car.refuel()
  car.stop()