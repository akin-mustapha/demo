from .extract import Extract
from .clean import Clean
from .transform import Transform
from .write import Write
from .null_process import NullProcess

processes = [Extract, Clean, Transform, Write, NullProcess]