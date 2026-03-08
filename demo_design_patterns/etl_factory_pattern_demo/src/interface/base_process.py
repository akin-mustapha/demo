from abc import ABC, abstractmethod


class BaseProcess(ABC):

  @abstractmethod
  def execute(self, **kwargs):
    pass