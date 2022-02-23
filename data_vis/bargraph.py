import numpy as np
import pandas as pd

from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

from typing import List
import json
import requests
 
ENDPOINT_DICT = {
  "BTC": "",
  "ETC": "",
  "LN": "https://1ml.com/node?json=true"
}

def call_api(endpoint: str):
  res = requests.get(endpoint)
  return res.json()

def preprocessing(data_list: json) -> List[int]:
  alias_list = []
  capacity_list = []
  for data in data_list:
    alias_list.append(data['alias'])
    capacity_list.append(data['capacity'])
  return alias_list, capacity_list

if __name__ == "__main__":
  json_data = call_api(ENDPOINT_DICT["LN"])
  alias_list, capacity_list = preprocessing(json_data)

  plt.bar(range(len(capacity_list)), capacity_list)

  plt.title("capacity of node")
  plt.ylabel("capacity")
  plt.xticks(range(len(alias_list)), alias_list)

  plt.show()
