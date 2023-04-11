import json
import csv
from tqdm import tqdm
import pandas as pd
import random

balance_qa = json.load(open("../anetqa/anetqa_train.json"))+json.load(open("../anetqa/anetqa_val.json"))+json.load(open("../anetqa/anetqa_test.json"))
keys=[]
questions=[]
answers=[]
vid_ids=[]
descriptions=[]
video ={}
for qa in tqdm(balance_qa):
    video_id=qa["qa_id"][:13]
    if video_id not in video:
        video[video_id]=[]
    video[video_id].append(qa)
print(len(video))
video_train =json.load(open("../jsons/video_train.json"))
video_val = json.load(open("../jsons/video_val.json"))
video_test =json.load(open("../jsons/video_test.json"))
video_train_val=video_train+video_val

for video_id in tqdm(video_train_val):
    if video_id not in video:
        print(video_id)
    else:
        for qa in video[video_id]:
            video_ids = qa["qa_id"]
            question = qa["question"]
            answer = qa["answer"]
            keys.append(video_ids)
            questions.append(question)
            answers.append(answer)
            vid_ids.append(video_id)
            descriptions.append("none")
print(len(questions)//len(video_train_val))
dic1 = {
    "key":keys,
    "question":questions,
    "answer":answers,
    "vid_id":vid_ids,
    "gif_name":vid_ids,
    "description":descriptions
}
df = pd.DataFrame(dic1)
print("------dump-------")
df.to_csv("../anetqa/data_train_val.csv")

keys=[]
questions=[]
answers=[]
vid_ids=[]
descriptions=[]
for video_id in tqdm(video_train):
    if video_id not in video:
        print(video_id)
    else:
        for qa in video[video_id]:
            video_ids = qa["qa_id"]
            question = qa["question"]
            answer = qa["answer"]
            keys.append(video_ids)
            questions.append(question)
            answers.append(answer)
            vid_ids.append(video_id)
            descriptions.append("none")
print(len(questions)//len(video_train))

dic1 = {
    "key":keys,
    "question":questions,
    "answer":answers,
    "vid_id":vid_ids,
    "gif_name":vid_ids,
    "description":descriptions
}
df = pd.DataFrame(dic1)
print("------dump-------")
df.to_csv("../anetqa/data_train.csv")

keys=[]
questions=[]
answers=[]
vid_ids=[]
descriptions=[]
for video_id in tqdm(video_val):
    for qa in video[video_id]:
        video_ids = qa["qa_id"]
        question = qa["question"]
        answer = qa["answer"]
        keys.append(video_ids)
        questions.append(question)
        answers.append(answer)
        vid_ids.append(video_id)
        descriptions.append("none")
print(len(questions)//len(video_val))

dic1 = {
    "key":keys,
    "question":questions,
    "answer":answers,
    "vid_id":vid_ids,
    "gif_name":vid_ids,
    "description":descriptions
}
df = pd.DataFrame(dic1)
print("------dump-------")
df.to_csv("../anetqa/data_val.csv")

keys=[]
questions=[]
answers=[]
vid_ids=[]
descriptions=[]
for video_id in tqdm(video_test):
    for qa in video[video_id]:
        video_ids = qa["qa_id"]
        question = qa["question"]
        answer=""
        keys.append(video_ids)
        questions.append(question)
        answers.append(answer)
        vid_ids.append(video_id)
        descriptions.append("none")
print(len(questions)//len(video_test))
dic2 = {
    "key":keys,
    "question":questions,
    "answer":answers,
    "vid_id":vid_ids,
    "gif_name":vid_ids,
    "description":descriptions
}
df = pd.DataFrame(dic2)
print("------dump-------")
df.to_csv("../anetqa/data_test.csv")