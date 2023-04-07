# all-in-one

Find the code and set-up instructions on the [all-in-one Github](https://github.com/showlab/all-in-one)

## Install Dependencies

### 1. PytorchLighting

In this work, we use PytorchLighting for distributed training with mixed precision. Install pytorch and PytorchLighting first.

```
conda create -n allinone python=3.7
source activate allinone
cd [Path_To_This_Code]
pip install -r requirements.txt
```

### 2. ffmpeg and pytorch video (may use)

#### 1. ffmpeg

```
sudo conda install -y ffmpeg
```

Please install the required packages if not included in the requirements.txt.

If you server cannot connect to http or install ffmpeg slowly. Please download static binary file from [FFmpeg Static Builds](https://johnvansickle.com/ffmpeg/) and then add to path variable, as follows:

```
export PATH=[PATH_TO_Dir/]ffmpeg-git-20220108-amd64-static:$PATH
```

#### 2. pytorch video

Install pytorchvideo (for data augmentation) as below:

```
pip install ffmpeg-python
pip install pytorchvideo
```

## Images

In consideration of training speed, we sample frames from the videos in the form of pictures for training.

For all-in-one, we sample the middle frames of each second from the video in the form of pictures. We randomly sample 3 frames for training and uniformly sample 3 frames for validation.

## Sample Images

- Download ActivityNet Videos [here](http://activity-net.org/) and train/val/test video list [here]()

- Use `sample_imgs_allinone.py` to sample images and place them in `data/acqa/frameqa`

- Revise the path in `AllInOne\datasets\tgif.py` 

  ```python
  /meta_data/imgs --->{store_path}/imgs
  /meta_data/val_imgs	--->{store_path}/val_imgs
  ```

- Download jsons that records the video duration and fps [here](), and place them `meta_data/tgif`

## Download qa pairs

Download qa pairs in .jsonl version [here]()

## Download Pretrained Weights

Download **All-in-one-B** [here](https://drive.google.com/file/d/1z3g891ND6CGCUkVzCXr2647wVG-15uUS/view?usp=sharing)

After downloaded these pretrained weights, move them into pretrained dir.

```
mkdir pretrained
cp *.ckpt pretrained/
```

## Run Model

Train

```
python run.py with data_root=DataSet num_gpus=4 num_nodes=1 num_frames=3 per_gpu_batchsize=32 task_finetune_tgifqa load_path="pretrained/all-in-one-base.ckpt"
```

**Note: as the anetqa format is similar to tgif-qa, the same config is used**

Test

```
python run.py with data_root=DataSet num_gpus=4 num_nodes=1 num_frames=3 per_gpu_batchsize=64 task_finetune_tgifqa test_only=True load_path=${ckpt_path}
```

#### View details of result

Download the list of qa_id under different classification systems [here]()

You can use them to analyze the details of the results

#### Updated and added code files

- AllInOne\datasets\tgif.py

- video_len.json

- video_fps.json

  