import numpy as np

from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

from typing import List
import json
import requests

from ..lib.data_loader import DataLoader

def preprocessing(data_list: json) -> List[int]:
  alias_list = []
  capacity_list = []
  for data in data_list:
    alias_list.append(data['alias'])
    capacity_list.append(data['capacity'])
  return alias_list, capacity_list

if __name__ == "__main__":
  data_loader = DataLoader.new(3)
  json_data = data_loader.get_data()
  alias_list, capacity_list = preprocessing(json_data)

  plt.bar(range(len(capacity_list)), capacity_list)

  plt.title("capacity of node")
  plt.ylabel("capacity")
  plt.xticks(range(len(alias_list)), alias_list)

  plt.show()
