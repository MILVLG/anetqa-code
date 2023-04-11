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

  place *.jsonl in `ClipBERT/` and `all-in-one/`

- sample frames for visualization

  ```
  python sample_frame_img.py
  ```

After that, the `datasets` folder will have the following structure:

```
datasets
├── videos
│   ├── ...
│   ├── VIDEO_ID.mp4/mkv
│   └── ...
├── anetsg
│   ├── anetsg_train.json 
│   └── anetsg_val.json
├── anetqa
│   ├── anetqa_train.json
|	├── anetqa_val.json
│   └── anetqa_test.json
├── jsons
│   ├── video_train.json
|	├── video_val.json
|	├── video_test.json
|	├── anetqa_object_class.json
|	├── anetqa_attribute_class.json
│   └── anetqa_relationship_class.json
└── scripts
	├── aux_csv.py
	├── aux.jsonl.py
    └── sample_frame_img.py
```

## Scene Graph Format

```json
{
     "v_onFddYAkyyc":{
         "objects":{
                    "v_onFddYAkyyc/0/4/53": {
                    "object_id": 53,
                    "object_class": "bathroom",
                    "bbox": [
                        2,
                        0,
                        714,
                        539
                    ],
                    "crowds": 0,
                    "video_id": "v_onFddYAkyyc",
                    "segment_id": "0",
                    "frame_id": "4"
                },
                "v_onFddYAkyyc/0/4/54": {
                    "object_id": 54,
                    "object_class": "person",
                    "bbox": [
                        403,
                        1,
                        266,
                        538
                    ],
                    "crowds": 0,
                    "video_id": "v_onFddYAkyyc",
                    "segment_id": "0",
                    "frame_id": "4"
                },
         },
         "attributes":{
                "v_onFddYAkyyc/0/4/53": {
                    "attribute_class": "object",
                    "color": [
                        "grey"
                    ],
                    "material": "none",
                    "shape": "none",
                    "status": "none",
                    "location": "none",
                    "covered_by": "none",
                    "filled_with": "none"
                },
                "v_onFddYAkyyc/0/4/54": {
                    "attribute_class": "person",
                    "age&sex": "boy",
                    "hair_style": "curly",
                    "hair_length": "short",
                    "hair_color": [
                        "brown"
                    ],
                    "headwear_color": [
                        "purple"
                    ],
                    "accessory": [
                        "bracelet",
                        "glove",
                        "ring"
                    ],
                    "skin_color": "white",
                    "upper_clothes_type": "t-shirt",
                    "upper_clothes_color": [
                        "black"
                    ],
                    "lower_clothes_type": "trousers",
                    "lower_clothes_color": [
                        "blue"
                    ],
                    "status": [
                        "working",
                        "dancing"
                    ],
                    "location": "indoors",
                    "occupation": "none",
                    "nationality": "none"
                },
         },
         "relationships":{
             {
                "subject": "v_onFddYAkyyc/0/4/54",
                "object": "v_onFddYAkyyc/0/4/53",
                "relationship_type": "contact",
                "relationship": "sweeping"},
             {
                "subject": "v_onFddYAkyyc/0/4/54",
                "object": "v_onFddYAkyyc/0/4/55",
                "relationship_type": "contact",
                "relationship": "holding"},
         },
         "actions":[            
             {
                 "duration": [
                     0.01,
                     62.99573696145125
                 ],
                 "anet_label": "mopping the floor"
             },
             {
                 "duration": [
                     0,
                     20.16
                 ],
                 "activity_caption": "a boy cleans a bathroom with a mop while dancing"
             }
        ]
     }
}
```

**Note: attributes have different formats depending on the singular or plural forms of objects.**

## QA Format

- **train/val**

  ```
  [...
       {'question': 'At the beginning of the video, what color is the cat indoors which is lying?',
        'answer': 'white',
        'qa_id': 'v_m7cHlmcFk9Y#attrWhat#2',
        'video_id': 'v_m7cHlmcFk9Y',
        'frame_ids': ['v_m7cHlmcFk9Y/0/0'],
        'object_ids': ['v_m7cHlmcFk9Y/0/0/52820'],
        'question_type': 'attrWhat',
        'attribute_type': 'color',
        'step': 5,
        'program': 'select(at the beginning of the video)->select(cat)->filter(location,indoors)->filter(status,lying)->query(color)'},
   ...]
  ```

- **test**

  ```
  [...
  	{
          'question': 'Does the girl in the cloak appear at the end of the video?',
    		'qa_id': 'v_Gq8-XVrlAt4#objExist#8503',
    		'video_id': 'v_Gq8-XVrlAt4',
    		'question_type': 'objExist',
    		'attribute_type': 'none'}
       }
   ...]
  ```

  