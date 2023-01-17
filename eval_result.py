import json
import xlwt

res_path = ""
dump_name = "result.xls"

res = json.load(open(res_path))
print(res_path)
print(dump_name)

nums_right={}
q_type_num_right={}
q_type_num_false={}
wbk = xlwt.Workbook()
sheet = wbk.add_sheet("1")
count=0
q_type_num_right["sequencing"]=0
q_type_num_false["sequencing"]=0
q_type_num_right["superlative"]=0
q_type_num_false["superlative"]=0
q_ids=[]
for qa in res:
    q_ids.append(qa["q_id"])
    q_type = qa["q_id"][13:qa["q_id"].find("*")]
    answer = qa["answer"]
    pred = qa["prediction"]
    if answer!=pred:
        if q_type not in q_type_num_false:
            q_type_num_false[q_type]=0
        q_type_num_false[q_type]+=1
    if answer==pred:
        if answer not in nums_right:
            nums_right[answer]=0
        nums_right[answer]+=1
        if q_type not in q_type_num_right:
            q_type_num_right[q_type]=0
        q_type_num_right[q_type]+=1
    question = " "+" ".join(qa["question"])+" "
    if "at the beginning" in question or "at the end" in question:
        if answer!=pred:
            q_type_num_false["superlative"]+=1
        if answer==pred:
            q_type_num_right["superlative"]+=1
    if " before " in question or " after " in question:
        if answer!=pred:
            q_type_num_false["sequencing"]+=1
        if answer==pred:
            q_type_num_right["sequencing"]+=1

types=["actExist","objExist","objRelExist",
        "attrRelWhat","attrWhat","relWhat","objRelWhere","objRelWhat","objWhere","objWhat",
        "objRelWhatChoose","objWhatChoose","attrWhatChoose","attrRelWhatChoose",
        "attrsame","attrcompare","actTime","actLongerVerify","actShorterVerify",
        "andObjRelExist","xorObjRelExist"]
structural={
    "query":["objWhat","objRelWhat","attrWhat","attrRelWhat","relWhat","objWhere","objRelWhere"],
    "compare":["attrsame","attrcompare","actTime","actLongerVerify","actShorterVerify"],
    "choose":["objWhatChoose","objRelWhatChoose","attrWhatChoose","attrRelWhatChoose",],
    "verify":["actExist","objExist","objRelExist"],
    "logic":["andObjRelExist","xorObjRelExist"]
}
overall={
    "binary":["actExist","objExist","objRelExist","andObjRelExist","xorObjRelExist","attrcompare","actTime","actLongerVerify","actShorterVerify"],
    "open":["objWhat","objRelWhat","attrWhat","attrRelWhat","relWhat","objWhere","objRelWhere","attrsame","objWhatChoose","objRelWhatChoose","attrWhatChoose","attrRelWhatChoose"],
    "overall":types
}
semantic={
    "object":["objWhatChoose","objRelWhatChoose","objWhat","objRelWhat","objExist"],
    "relationship":["andObjRelExist","xorObjRelExist","objRelExist","relWhat","objWhere","objRelWhere"],
    "attribute":["attrWhatChoose","attrRelWhatChoose","attrWhat","attrRelWhat","attrsame","attrcompare"],
    "action":["actExist","actTime","actLongerVerify","actShorterVerify"]
}
reasoning={
    "object-relation":["objRelWhatChoose","attrRelWhatChoose",
                        "relWhat","objWhere","objRelWhere","objRelWhat","attrRelWhat",
                        "objRelExist",
                        "andObjRelExist","xorObjRelExist"],
    "object-attribute":["objRelWhatChoose","objWhatChoose","attrWhatChoose","attrRelWhatChoose",
                        "objWhat","objRelWhat","attrWhat","attrRelWhat","relWhat","objWhere","objRelWhere",
                        "objExist","objRelExist","andObjRelExist","xorObjRelExist","attrsame","attrcompare"],
    "duration-comparison":["actLongerVerify","actShorterVerify"],
    "exist":["actExist","objExist","objRelExist","andObjRelExist","xorObjRelExist"],
    "sequencing":["sequencing"],
    "superlative":["superlative"]
}

for qtype in types:
    sheet.write(count,2,qtype)
    sheet.write(count,3,q_type_num_right[qtype]/(q_type_num_right[qtype]+q_type_num_false[qtype]))
    sheet.write(count,4,q_type_num_right[qtype])
    sheet.write(count,5,q_type_num_right[qtype]+q_type_num_false[qtype])
    count+=1
    print(qtype,"{:.2%}".format(q_type_num_right[qtype]/(q_type_num_right[qtype]+q_type_num_false[qtype])),q_type_num_right[qtype]+q_type_num_false[qtype])

for i in structural:
    countall=0
    counttrue=0
    for qtype in structural[i]:
        counttrue+=q_type_num_right[qtype]
        countall +=q_type_num_right[qtype]
        countall +=q_type_num_false[qtype]
    sheet.write(count,2,i)
    sheet.write(count,3,counttrue/countall*100)
    sheet.write(count,4,counttrue)
    sheet.write(count,5,countall)
    count+=1
    print(i,"{:.2%}".format(counttrue/countall),countall)
for i in semantic:
    countall=0
    counttrue=0
    for qtype in semantic[i]:
        counttrue+=q_type_num_right[qtype]
        countall +=q_type_num_right[qtype]
        countall +=q_type_num_false[qtype]
    sheet.write(count,2,i)
    sheet.write(count,3,counttrue/countall*100)
    sheet.write(count,4,counttrue)
    sheet.write(count,5,countall)
    count+=1
    print(i,"{:.2%}".format(counttrue/countall),countall)
for i in reasoning:
    countall=0
    counttrue=0
    for qtype in reasoning[i]:
        counttrue+=q_type_num_right[qtype]
        countall +=q_type_num_right[qtype]
        countall +=q_type_num_false[qtype]
    sheet.write(count,2,i)
    sheet.write(count,3,counttrue/countall*100)
    sheet.write(count,4,counttrue)
    sheet.write(count,5,countall)
    count+=1
    print(i,"{:.2%}".format(counttrue/countall),countall)
for i in overall:
    countall=0
    counttrue=0
    for qtype in overall[i]:
        counttrue+=q_type_num_right[qtype]
        countall +=q_type_num_right[qtype]
        countall +=q_type_num_false[qtype]
    sheet.write(count,2,i)
    sheet.write(count,3,counttrue/countall*100)
    sheet.write(count,4,counttrue)
    sheet.write(count,5,countall)
    count+=1
    print(i,"{:.2%}".format(counttrue/countall),countall)

wbk.save(dump_name)