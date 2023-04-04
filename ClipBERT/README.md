### ClipBERT

Find the code and set-up instructions on the [ClipBERT Github](https://github.com/jayleicn/ClipBERT)

ClipBERT use .jsonl version

### Images

In consideration of training speed, we sample frames from the videos in the form of pictures for training.

For ClipBERT, we randomly sample 5 sets of 4x2 frames  for training and uniformly sample 16 frames for validation.

```
python sample_imgs_clipbert.py
```

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

