# HCRN

The HCRN implementation is derived from the [official repo](https://github.com/thaolmk54/hcrn-videoqa) and adapt to ANetQA

## Install Dependencies

```
conda create -n hcrn_videoqa python=3.6
conda activate hcrn_videoqa
conda install -c conda-forge ffmpeg
conda install -c conda-forge scikit-video
pip install -r requirements.txt
```

## modify the file format of qa pairs

```
python aux_csv.py
```

place *.csv in `data/anetqa`

## Preprocessing visual features

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

1. Train:

   ```
   python train.py --cfg configs/anetqa.yml
   ```

2. Test:

   ```
   python validate.py --cfg configs/anetqa.yml
   ```

   If you want to use our checkpoint for testing, you can change the checkpoint path in `validate.py` on `line 96`

3. View details of result:

   ```
   python eval_res.py
   ```
