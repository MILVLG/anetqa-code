import json
import csv
from tqdm import tqdm
import pandas as pd
import random


train_val = pd.read_csv("data_train.csv")
val = pd.read_csv("data_val.csv")
test = pd.read_csv("data_test.csv")


train_val.to_json("data_train.jsonl",orient="records",lines=True)
val.to_json("data_val.jsonl",orient="records",lines=True)
test.to_json("data_test.jsonl",orient="records",lines=True)
