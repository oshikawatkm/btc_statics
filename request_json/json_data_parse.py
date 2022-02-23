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

if __name__ == "__main__":
  json_data = call_api(ENDPOINT_DICT["LN"])
  print(json_data)