from ..interface.base_process import BaseProcess
import pandas as pd

class Clean(BaseProcess):
  
  def execute(self, **kwargs):
    df = kwargs.get("data", pd.DataFrame)

    return df.dropna()