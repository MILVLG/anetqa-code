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
    if qa["taxonomy"]["question structures"] not in structures:
        structures[qa["taxonomy"]["question structures"]]=[]
    structures[qa["taxonomy"]["question structures"]].append(qa["qa_id"])
    if qa["taxonomy"]["question semantics"] not in semantics:
        semantics[qa["taxonomy"]["question semantics"]]=[]
    semantics[qa["taxonomy"]["question semantics"]].append(qa["qa_id"])
    for i in qa["taxonomy"]["reasoning skills"]:
        if i not in reasoning :
            reasoning [i]=[]
        reasoning [i].append(qa["qa_id"])
    if qa["taxonomy"]["answer types"] not in ans_type:
        ans_type[qa["taxonomy"]["answer types"]]=[]
    ans_type[qa["taxonomy"]["answer types"]].append(qa["qa_id"])
    val_gt[qa["qa_id"]]=qa["answer"]

ans={}
for i in res:
    qa_id = i["q_id"]
    pred = i["prediction"]
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