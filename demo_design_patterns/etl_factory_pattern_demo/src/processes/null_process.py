from ..interface.base_process import BaseProcess


class NullProcess(BaseProcess):
  def execute(self, **kwargs):
    print('Process not implemented')