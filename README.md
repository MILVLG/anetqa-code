# Code for ANetQA baselines

This repository contains code for our baselines HCRN, ClipBERT, and all-in-one. For all three baselines, we used their code for the FrameQA questions in the TGIF-QA benchmark, then adjusted to fit our data structure. You can download ANetQA from our [website](https://milvlg.github.io/anetqa).

## results

| val acc | hcrn  | ClipBERT | all-in-one-base |
| ------- | ----- | -------- | --------------- |
| overall | 41.69 | 44.34    | 45.44           |

## Data

### Videos

You can download ActivityNet videos [here](http://activity-net.org/)

### Appearance Features

We shared appearance features across models for consistency (RESNET for appearance and RESNEXT for accuracy). Find the visual features stored [here](). The file names are the same as the original baselines (so they reference tgif-qa). However, these files include the features for the videos used in ANETQA.

- acqa_frameqa_appearance_feat.h5（12GB）
- acqa_frameqa_motion_feat.h5（721MB）

### Images

In consideration of training speed, we sample frames from the videos in the form of pictures for training.

For ClipBERT, we randomly sample 5 sets of 4x2 frames  for training and uniformly sample 16 frames for validation.

For all-in-one, we sample the middle frames of each second from the video in the form of pictures. We randomly sample 3 frames for training and uniformly sample 3 frames for validation.

Use `sample_imgs_clipbert.py` and  `sample_img_allinone`.py to sample imges

### Questions formatted

HCRN use .csv version, both ClipBERT and all-in-one use .jsonl version. you can find the questions in a .csv and .jsonl format stored [here]()

## Models

### HCRN

Find the code and set-up instructions on the [HCRN Github](https://github.com/thaolmk54/hcrn-videoqa)

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

### ClipBERT

Find the code and set-up instructions on the [ClipBERT Github](https://github.com/jayleicn/ClipBERT)

#### Sample Images

- Download ActivityNet Videos [here](http://activity-net.org/) and train/val/test video list [here]()
- Use `sample_imgs_clipbert.py` to sample images

- Revise the path in `src\datasets\dataset_base.py` 

  ```python
  pickle.load(open(${img_path}),"rb")
  ```

#### Run Model

Train:`horovodrun -np 4 python src/tasks/run_video_qa.py --config src/configs/tgif_qa_frameqa_base_resnet50.json --output_dir ./result`

Test:`horovodrun -np 4 python src/tasks/run_video_qa.py --config src/configs/tgif_qa_frameqa_base_resnet50.json  --do_inference 1 --output_dir $OUTPUT_DIR   --inference_split val --inference_model_step $STEP --inference_txt_db /txt/data_test.jsonl  --inference_batch_size 64 --inference_n_clips 16`

#### Updated and added code files

- src/task/run_video_qa.py
- src/datasets/dataset_base.py
- src/configs/tgif_qa_frameqa_base_resnet50.json
- src/datasets/dataset_video_qa.py
- src/utils/load_save.py

### all-in-one

Find the code and set-up instructions on the [all-in-one Github](https://github.com/showlab/all-in-one)

#### Sample Images

- Download ActivityNet Videos [here](http://activity-net.org/) and train/val/test video list [here]()
- Use `sample_imgs_allinone.py` to sample images and place them in `data/acqa/frameqa`

- Revise the path in `AllInOne\datasets\tgif.py` 

  ```python
  /meta_data/imgs --->{store_path}/imgs
  /meta_data/val_imgs	--->{store_path}/val_imgs
  ```

- Download jsons that records the video duration and fps [here](), and place them `meta_data/tgif`

#### Run Model

Train: `python run.py with data_root=DataSet num_gpus=4 num_nodes=1 num_frames=3 per_gpu_batchsize=32 task_finetune_tgifqa load_path="pretrained/all-in-one-base.ckpt"`

Test:`python run.py with data_root=DataSet num_gpus=4 num_nodes=1 num_frames=3 per_gpu_batchsize=64 task_finetune_tgifqa test_only=True load_path=${ckpt_path}`

#### Updated and added code files

- AllInOne\datasets\tgif.py

- video_len.json

- video_fps.json

  