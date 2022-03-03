
import requests
import json
from typing import List
DATA_TYPE = {
  1: "BTC",
  2: "ETC",
  3: "LN"
}

ENDPOINT_DICT = {
  "BTC": "",
  "ETC": "",
  "LN": "https://1ml.com/node?json=true"
}

class DataLoader:
  def __init__(self, date_type: int) -> None:
    self.data_type = date_type

  def get_preprpcessed_data(self, attribute_name_1: str, addribute_name_2: str) -> json:
    json_data = self.get_data()
    preprocessed_data = self.preprocess(json_data, attribute_name_1, addribute_name_2)
    return preprocessed_data

  def get_data(self) -> json:
    response = requests.get(ENDPOINT_DICT[DATA_TYPE[self.data_type]])
    return response.json()

  def preprocess(self, json_data: json, attribute_name_1: str, addribute_name_2: str) -> List[int]:
    alias_list = []
    capacity_list = []
    for data in json_data:
      alias_list.append(data[attribute_name_1])
      capacity_list.append(data[addribute_name_2])
    return alias_list, capacity_list