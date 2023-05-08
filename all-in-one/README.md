# all-in-one

The All-in-one implementation is derived from the [official repo](https://github.com/showlab/all-in-one) and adapt to ANetQA.

## Install Dependencies

### 1. PytorchLighting

In this work, we use PytorchLighting for distributed training with mixed precision. Install pytorch and PytorchLighting first.

```
conda create -n allinone python=3.7
source activate allinone
cd [Path_To_This_Code]
pip install -r requirements.txt
```

**Note: Installing apex using pip may fail, see [NVIDIA/apex](https://github.com/NVIDIA/apex) for installation details **

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

- Download ActivityNet Videos and train/val/test video list based on [dataset](https://github.com/MILVLG/anetqa-code/tree/main/dataset)

- Use `sample_imgs_allinone.py` to sample images and place them in `data/anetqa/frameqa`

- Revise the path in `AllInOne\datasets\tgif.py` 

  ```python
  meta_data/imgs --->{store_path}/imgs
  meta_data/val_imgs --->{store_path}/val_imgs
  ```

## modify the file format of qa pairs

```
python aux_csv.py
python aux_jsonl.py
```

place *.jsonl in`meta_data/anetqa/`

## Download Pretrained Weights

Download **All-in-one-B** [here](https://drive.google.com/file/d/1z3g891ND6CGCUkVzCXr2647wVG-15uUS/view?usp=sharing)

After downloaded these pretrained weights, move them into pretrained dir.

```
mkdir pretrained
cp *.ckpt pretrained/
```

## Run Model

1. Finetuning

   ```
   python run.py with data_root=DataSet num_gpus=4 num_nodes=1 num_frames=3 per_gpu_batchsize=32 task_finetune_anetqa load_path="pretrained/all-in-one-base.ckpt"
   ```

2. Run inference

   ```
   python run.py with data_root=DataSet num_gpus=4 num_nodes=1 num_frames=3 per_gpu_batchsize=64 task_finetune_anetqa test_only=True load_path=${ckpt_path}
   ```

3. View details of result

   ```
   python eval_res.py
   ```
  
