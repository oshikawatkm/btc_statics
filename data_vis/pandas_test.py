import numpy as np
import pandas as pd
from pandas import Series,DataFrame

from ..lib.data_loader import DataLoader

if __name__ == "__main__":
  data_loader = DataLoader.new(3)
  alias_list, capacity_list = data_loader.get_preprocessed_data('alias', 'capacity')
  cas = Series(capacity_list, index = alias_list)
  print(cas)