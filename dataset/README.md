# Dataset

## Videos and QA pairs

- Download ActivityNet videos [here](http://activity-net.org/) and place them in `videos`

- Download our scene graph from our [website](https://milvlg.github.io/anetqa/) and place them in `anetsg`

- Download our Question-Answer pairs from our [website](https://milvlg.github.io/anetqa/) and place them in `anetqa`

- Download [Meta information](https://awma1-my.sharepoint.com/:u:/g/personal/yuz_l0_tn/EZbBImoXyF1AstMYCqKwzIsBkfjoaYE2p9HtESIWaGDHmA?download=1) of all scene graphs and place them in `jsons`

- Download [Meta information](https://awma1-my.sharepoint.com/:u:/g/personal/yuz_l0_tn/EYIaBMbntepBt2tiG7USPO8Byi3ap-MkltQNdtUh9vZ2_w?download=1) of all videos and place them in `jsons`

- modify the file format of qa pairs for training (need video list)

  ```
  python aux_csv.json			#hcrn
  python aux_jsonl.json		#ClipBERT all-in-one
  ```

  place *.csv in `hcrn/data/anetqa`

  place *.jsonl in `ClipBERT/$PATH_TO_STORAGE` and `all-in-one/meta_data/anetqa/`

- sample frames for visualization

  ```
  python sample_frame_img.py
  ```

After that, the `datasets` folder will have the following structure:
