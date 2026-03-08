import logging
import os
from pathlib import Path
from dataclasses import dataclass, asdict
from datetime import datetime

import pandas as pd

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO, filemode="w", filename="info.log")

@dataclass
class File:
  name: str
  path: str
  extension: str
  
  

def crawl_path(root_path: str):
    for file_path in Path(root_path).rglob("*"):
        if file_path.is_file():
            stat = file_path.stat()

            # Modified time (reliable everywhere)
            modified_time = datetime.fromtimestamp(stat.st_mtime)

            # Created time (platform dependent)
            if hasattr(stat, "st_birthtime"):  # macOS
                created_time = datetime.fromtimestamp(stat.st_birthtime)
            else:
                created_time = datetime.fromtimestamp(stat.st_ctime)

            yield {
                "name": file_path.stem,
                "extension": file_path.suffix,
                "path": str(file_path),
                "size_bytes": stat.st_size,
                "created_at": created_time,
                "modified_at": modified_time,
            }
        
if __name__ == "__main__":
  root = "/Users/kunmi/Downloads"
  
  root_path = Path(root)
    
  paths = crawl_path(root)
  
  paths_df = pd.DataFrame(paths)
  print(paths_df.head(5))
  
  logger.info("hello world")