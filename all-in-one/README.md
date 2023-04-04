### all-in-one

Find the code and set-up instructions on the [all-in-one Github](https://github.com/showlab/all-in-one)

all-in-one use .jsonl version

### Images

In consideration of training speed, we sample frames from the videos in the form of pictures for training.

For all-in-one, we sample the middle frames of each second from the video in the form of pictures. We randomly sample 3 frames for training and uniformly sample 3 frames for validation.

```
python sample_img_allinone.py
```

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

  