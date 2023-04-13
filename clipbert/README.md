# ClipBERT

Find the code and set-up instructions on the [ClipBERT Github](https://github.com/jayleicn/ClipBERT)

## Images

In consideration of training speed, we sample frames from the videos in the form of pictures for training.

For ClipBERT, we randomly sample 5 sets of 4x2 frames  for training and uniformly sample 16 frames for validation.

## Sample Images

- Download ActivityNet Videos and train/val/test video list based on [dataset](https://github.com/MILVLG/anetqa-code/tree/main/dataset)
- Use `sample_imgs_clipbert.py` to sample images

- Revise the path in `src\datasets\dataset_base.py` 

  ```python
  pickle.load(open(${img_path}),"rb")
  ```

## modify the file format of qa pairs

```
python aux_csv.py
python aux_jsonl.py
```

place *.jsonl in `ClipBERT/$PATH_TO_STORAGE` 

## Requirements

We provide a Docker image for easier reproduction. Please install the following:

- [nvidia driver](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#package-manager-installation) (418+),
- [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) (19.03+),
- [nvidia-container-toolkit](https://github.com/NVIDIA/nvidia-docker#quickstart).

Our scripts require the user to have the [docker group membership](https://docs.docker.com/install/linux/linux-postinstall/) so that docker commands can be run without sudo. We only support Linux with NVIDIA GPUs. We test on Ubuntu 18.04 and V100 cards. We use mixed-precision training hence GPUs with Tensor Cores are recommended.

## Getting Started

1. Create a folder that stores pretrained models, all the data, and results.

   ```
   PATH_TO_STORAGE=/path/to/your/data/
   mkdir -p $PATH_TO_STORAGE/txt_db  # annotations
   mkdir -p $PATH_TO_STORAGE/vis_db  # image and video 
   mkdir -p $PATH_TO_STORAGE/finetune  # finetuning results
   mkdir -p $PATH_TO_STORAGE/pretrained  # pretrained models
   ```

2. Download pretrained models.

   e2e pretrained ClipBERT model (849MB), can be downloaded with the following command.

   ```
   bash scripts/download_pretrained.sh $PATH_TO_STORAGE
   ```

   This pretrained model can be used for finetuning on video-text tasks and image-text tasks. For your convenience, this script will also download `bert-base-uncased` and `grid-feat-vqa` model weights, which are used as initialization for pretraining.

3. Launch the Docker container for running the experiments.

   ```
   # docker image should be automatically pulled
   source launch_container.sh $PATH_TO_STORAGE/txt_db $PATH_TO_STORAGE/vis_db \
       $PATH_TO_STORAGE/finetune $PATH_TO_STORAGE/pretrained
   ```

   The launch script respects $CUDA_VISIBLE_DEVICES environment variable. Note that the source code is mounted into the container under `/clipbert` instead of built into the image so that user modification will be reflected without re-building the image. (Data folders are mounted into the container separately for flexibility on folder structures.)

## Run Model

1. Finetuning

   ```
   # inside the container
   horovodrun -np 4 python src/tasks/run_video_qa.py \
       --config src/configs/anetqa_frameqa_base_resnet50.json \
       --output_dir ./result
   ```

2. Run inference

   ```
   # inside the container
   horovodrun -np 4 python src/tasks/run_video_qa.py \
     --config src/configs/anetqa_frameqa_base_resnet50.json \
     --do_inference 1 --output_dir ./result \
     --inference_split val --inference_model_step $STEP \
     --inference_txt_db /txt/data_test.jsonl \
     --inference_batch_size 64 \
     --inference_n_clips 16 \
   ```

   `$STEP` is an integer, which tells the script to use the checkpoint (in our experiment `$STEP` is 163400)

3. View details of result:

   ```
   python eval_res.py
   ```

## Updated and added code files

- src/task/run_video_qa.py
- src/datasets/dataset_base.py
- src/datasets/dataset_video_qa.py
- src/utils/load_save.py

