import yaml 
from .src.factory.process_factory import ProcessFactory



if __name__ == "__main__":
  with open("etl_factory_pattern_demo/config.yaml") as f:
    config = yaml.safe_load(f)

  datasets = config.get('dataset', {})
  processes = config.get('processes', {})
  output = config.get('output', {})
  factory = ProcessFactory()
  factory.load_processes()

  i = []
  for dataset in datasets:
    extract = factory.get_process("extract")

    data = extract.execute(path=dataset.get("path", ''))

    clean = factory.get_process("clean")
    data = clean.execute(data=data)

    i.append(data)

  transform = factory.get_process("transform")
  transformed_data = transform.execute(*i)

  write = factory.get_process("write")
  write.execute(data=transformed_data, name=output.get("name"), path=output.get("path", ''))
  print(transformed_data)