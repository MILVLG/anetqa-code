# Code for ANETQA baselines

This repository contains code for our baselines HCRN, ClipBERT, and all-in-one. For all three baselines, we used their code for the FrameQA questions in the TGIF-QA benchmark, then adjusted to fit our data structure.

## results

| val acc | hcrn | hcrn w/o vision | ClipBERT | ClipBERT w/o vision | all-in-one-base | all-in-one-base w/o vision |
| ------- | ---- | --------------- | -------- | ------------------- | --------------- | -------------------------- |
| open    |      |                 |          |                     |                 |                            |
| binary  |      |                 |          |                     |                 |                            |
| overall |      |                 |          |                     |                 |                            |

## Data

### Appearance Features

We shared appearance features across models for consistency (RESNET for appearance and RESNEXT for accuracy). Find the visual features stored [here](). The file names are the same as the original baselines (so they reference tgif-qa). However, these files include the features for the videos used in ANETQA.

- tgif-qa_frameqa_appearance_feat.h5
- tgif-qa_frameqa_motion_feat.h5

### Images

For ClipBERT and all-in-one, both of them need sample images from videos, in consideration of training speed, we sampled the first and the last two frames of each second from the video in the form of pictures for training.(you'd better store them in ssd)

You can download ActivityNet videos [here]()

#### sample images

```python
python sample_imgs.py
```

### Questions formatted

HCRN use .csv version, both ClipBERT and all-in-one use .jsonl version. you can find the questions in a .csv and .jsonl format stored [here]() 

## Models

### HCRN

Find the code and set-up instructions on the [HCRN Github](https://github.com/thaolmk54/hcrn-videoqa)

#### Download Features

Download visual features from [here](), and place them in `data/acqa/frameqa`

#### Preprocess questions

Train_val: `python preprocess/preprocess_questions.py --dataset tgif-qa --question_type frameqa --glove_pt data/glove/glove.840.300d.pkl --mode train`

#### Run model

##### w version

```python
python train.py --cfg configs/acqa.yml
```

##### w/o version

- remove the annotation under the `blind version` in the file `DataLoader.py`

```python
python train.py --cfg configs/acqa_blind.yml
```

#### View details of result

- change the path of val results

```python
python eval_result.py
```

#### Updated and added code files

- configs/acqa.yml
- configs/acqa_blind.yml
- DataLoader.py
- train.py
- validate.py
- preprocess/preprocess_question.py
- preprocess/datautils/tgif_qa.py

#### Appearance features

- tgif-qa_frameqa_appearance_feat.h5
- tgif-qa_frameqa_motion_feat.h5

### ClipBERT



### all-in-one