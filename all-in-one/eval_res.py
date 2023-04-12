import json
from tqdm import tqdm

val_qas = json.load(open("../dataset/anetqa/qa_val.json"))
res_path=""
res = json.load(open(f"{res_path}"))

structures={}
semantics={}
reasoning={}
ans_type={}
val_gt={}
for qa in tqdm(val_qas):
    for i in qa["taxonomy"]["question structures"]:
        if i not in structures:
            structures[i]=[]
        structures[i].append(qa["qa_id"])
    for i in qa["taxonomy"]["question semantics"]:
        if i not in semantics:
            semantics[i]=[]
        semantics[i].append(qa["qa_id"])
    for i in qa["taxonomy"]["reasoning skills"]:
        if i not in reasoning :
            reasoning [i]=[]
        reasoning [i].append(qa["qa_id"])
    for i in qa["taxonomy"]["answer types"]:
        if i not in ans_type:
            ans_type[i]=[]
        ans_type[i].append(qa["qa_id"])
    val_gt[qa["qa_id"]]=qa["answer"]

ans={}
for i in res:
    qa_id = i["question_id"]
    pred = i["answer"]
    gt = val_gt[qa_id]
    if pred==gt:
        ans[qa_id]=1
    else:
        ans[qa_id]=0

taxs = [structures,semantics,reasoning,ans_type]
for tax in taxs:
    for i in tax:
        count=0
        for j in tax[i]:
            count+=ans[j]
        print(i,count/len(tax[i]))
count=0
for i in ans:
    count+=ans[i]
print("overall",count/len(ans))