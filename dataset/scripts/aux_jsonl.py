import json
import csv
from tqdm import tqdm
import pandas as pd
import random


train_val = pd.read_csv("../anetqa/data_train.csv")
val = pd.read_csv("../anetqa/data_val.csv")
test = pd.read_csv("../anetqa/data_test.csv")


train_val.to_json("../anetqa/data_train.jsonl",orient="records",lines=True)
val.to_json("../anetqa/data_val.jsonl",orient="records",lines=True)
test.to_json("../anetqa/data_test.jsonl",orient="records",lines=True)
