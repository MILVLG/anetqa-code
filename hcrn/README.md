# HCRN

Find the code and set-up instructions on the [HCRN Github](https://github.com/thaolmk54/hcrn-videoqa)

## Install Dependencies

```
conda create -n hcrn_videoqa python=3.6
conda activate hcrn_videoqa
conda install -c conda-forge ffmpeg
conda install -c conda-forge scikit-video
pip install -r requirements.txt
```

## Download Features and qa pairs

Download visual features from [here](), and place them in `data/anetqa/frameqa`

Download qa pairs in .csv  version [here]()， and place them in `data/anetqa`

## Preprocessing visual features

You can also extract features yourself as follows:

revise the `video_dir` in `preprocess/preprocess_feature.py`

1. To extract appearance feature:

   ```
   python preprocess/preprocess_features.py --gpu_id 0 --dataset anetqa --model resnet101 --question_type frameqa
   ```

2. To extract motion feature:

   Download ResNeXt-101 [pretrained model](https://drive.google.com/drive/folders/1zvl89AgFAApbH0At-gMuZSeQB_LpNP-M) (resnext-101-kinetics.pth) and place it to `data/preprocess/pretrained/`.

   ```
   python preprocess/preprocess_features.py --dataset anetqa --model resnext101 --image_height 112 --image_width 112 --question_type frameqa
   ```

## Preprocess questions

1. Download [glove pretrained 300d word vectors](http://nlp.stanford.edu/data/glove.840B.300d.zip) to `data/glove/` and process it into a pickle file:

   ```
   python txt2pickle.py
   ```

2. Preprocess train/val/test questions:

   Train_val

   ```
   python preprocess/preprocess_questions.py --dataset anetqa --question_type frameqa --glove_pt data/glove/glove.840.300d.pkl --mode train
   ```

   Test: 

   ```
   python preprocess/preprocess_questions.py --dataset anetqa --question_type frameqa --mode test
   ```

## Run model

Train:

```
python train.py --cfg configs/anetqa.yml
```

Test:

```
python validate.py --cfg configs/anetqa.yml
```

## View details of result

Download the list of qa_id under different classification systems [here]()

You can use them to analyze the details of the results

## Updated and added code files

- configs/anetqa.yml
- DataLoader.py
- train.py
- validate.py
- preprocess/preprocess_question.py
- preprocess/datautils/tgif_qa.py
