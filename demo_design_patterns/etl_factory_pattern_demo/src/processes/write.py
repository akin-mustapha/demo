from ..interface.base_process import BaseProcess
import pandas as pd
from pathlib import Path

class Write(BaseProcess):

  def execute(self, **kwargs):
    path = Path(kwargs.get('path', ''))

    path.mkdir()
    kwargs.get('data', pd.DataFrame).to_csv(f"{path}/{kwargs.get('name')}.csv")