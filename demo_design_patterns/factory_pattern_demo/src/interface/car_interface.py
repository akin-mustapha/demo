from abc import ABC, abstractmethod

class CarInterface (ABC):
  
  @property
  @abstractmethod
  def model_name(self):
    pass
  
  @model_name.setter
  def model_name(self, model_name: str):
    self.model_name = model_name

  @classmethod
  @abstractmethod
  def start(self):
    pass

  @classmethod
  @abstractmethod
  def refuel(self, liter: float):
    pass

  @classmethod
  @abstractmethod
  def stop(self):
    pass