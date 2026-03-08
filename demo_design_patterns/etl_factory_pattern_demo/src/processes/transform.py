from ..interface.base_process import BaseProcess
import pandas as pd
class Transform(BaseProcess):

  def execute(self, *args):
    return pd.merge(left=args[0], right=args[1], how="inner", on='id')
  

if __name__ == "__main__":
  cls = Transform()

  data = cls.execute(pd.DataFrame([1,2,3,4], columns=["id"]), pd.DataFrame([1,2,3,4], columns=["id"]))
  print(data)
