from ..interface.base_process import BaseProcess
import pandas as pd

class Extract(BaseProcess):

  def __init__(self):
    super().__init__()

  def execute(self, **kwargs):
    data = pd.read_csv(kwargs.get("path", ""))
    
    return data
  

if __name__ == "__main__":
  cls = Extract()
  data = cls.execute(path='./etl_factory_pattern_demo/data/data.csv')
  print(data)