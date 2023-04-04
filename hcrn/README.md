### HCRN

Find the code and set-up instructions on the [HCRN Github](https://github.com/thaolmk54/hcrn-videoqa)

HCRN use .csv version

### Appearance Features

We shared appearance features across models for consistency (RESNET for appearance and RESNEXT for accuracy). Find the visual features stored [here](). The file names are the same as the original baselines (so they reference tgif-qa). However, these files include the features for the videos used in ANETQA.

- acqa_frameqa_appearance_feat.h5（12GB）
- acqa_frameqa_motion_feat.h5（721MB）

#### Download Features

Download visual features from [here](), and place them in `data/acqa/frameqa`

#### Preprocess questions

Train_val: `python preprocess/preprocess_questions.py --dataset tgif-qa --question_type frameqa --glove_pt data/glove/glove.840.300d.pkl --mode train`

Test: `python preprocess/preprocess_questions.py --dataset tgif-qa --question_type frameqa --mode test`

#### Run model

Train:`python train.py --cfg configs/acqa.yml`

Test:`python validate.py --cfg configs/acqa.yml`

#### View details of result

Download the list of qa_id under different classification systems [here]()

you can use them to analyze the details of the results

#### Updated and added code files

- configs/acqa.yml
- DataLoader.py
- train.py
- validate.py
- preprocess/preprocess_question.py
- preprocess/datautils/tgif_qa.py

#### Appearance features

- tgif-qa_frameqa_appearance_feat.h5
- tgif-qa_frameqa_motion_feat.h5
