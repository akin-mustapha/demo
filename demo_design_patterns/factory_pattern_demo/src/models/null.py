from ..interface.car_interface import CarInterface


class Null(CarInterface):

  def model_name(self):
    return "Null"

  def start(self):
    print("Can not start car, car model not implemented")
  
  def refuel(self, liter):
    print("Can not refuel car, car model not implemented")
  
  def stop(self):
    print("Car model not implemented")