# Dataset

## Videos and QA pairs

1. Download ActivityNet videos [here](http://activity-net.org/) and unzip them into the `dataset/video` folder
2. Download our scene graph from our [website](https://milvlg.github.io/anetqa/) and unzip them into the `dataset/sg` folder
3. Download our Question-Answer pairs from our [website](https://milvlg.github.io/anetqa/) and unzip them into the `dataset/qa` folder
4. Download [Meta information](https://awma1-my.sharepoint.com/:u:/g/personal/yuz_l0_tn/EZbBImoXyF1AstMYCqKwzIsBkfjoaYE2p9HtESIWaGDHmA?download=1) of all scene graphs and unzip them into the `dataset/meta` folder.
5. Download [Meta information](https://awma1-my.sharepoint.com/:u:/g/personal/yuz_l0_tn/EYIaBMbntepBt2tiG7USPO8Byi3ap-MkltQNdtUh9vZ2_w?download=1) of all videos and unzip them into the `dataset/meta` folder.

After that, the `dataset` folder will have the following structure:

```
dataset
├── video
│   ├── ...
│   ├── VIDEO_ID.mp4(mkv)
│   └── ...
├── sg
│   ├── sg_train.json 
│   └── sg_val.json
├── qa
│   ├── qa_train.json
|   ├── qa_val.json
│   └── q_test.json
├── meta
│   ├── video_train.json
|   ├── video_val.json
|   ├── video_test.json
|   ├── frames_trainval.json
|   ├── object_class.json
|   ├── attribute_class.json
│   └── relationship_class.json
```

After the data preparation, you can sample some selected frames and visualize the scene graph on it using the following script

```
python src/sample_frame_img.py
```

## Scene Graph Format

The `sg_train.json` and `sg_val.json` files have the following structure:
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
Note that attributes have slight different formats when the `crowds` option is set to different flags.

## QA Format

The `qa_train.json` and `qa_val.json` files have the following structure:

```
[
   {
        'question': 'At the beginning of the video, what color is the cat indoors which is lying?',
        'answer': 'white',
        'qa_id': 'v_m7cHlmcFk9Y#attrWhat#2',
        'video_id': 'v_m7cHlmcFk9Y',
        'frame_ids': ['v_m7cHlmcFk9Y/0/0'],
        'object_ids': ['v_m7cHlmcFk9Y/0/0/52820'],
        'attribute_type': 'color',
        'step': 5,
        'program': 'select(at the beginning of the video)->select(cat)->filter(location,indoors)->filter(status,lying)->query(color)',
        'taxonomy': {
            'question_type':'attrWhat',
            'question structures': 'query', 
            'question semantics': 'attribute', 
            'reasoning skills': ['object-attribute', 'superlative'], 
            'answer types': 'open'
        }
    }
]
```

The `q_test.json` file has the following structure:

```
[
   {
        'question': 'Does the girl in the cloak appear at the end of the video?',
        'qa_id': 'v_Gq8-XVrlAt4#objExist#8503',
        'video_id': 'v_Gq8-XVrlAt4',
        'attribute_type': 'none',
        'taxonomy': {
            'question_type':'objExist',
            'question structures': 'verify', 
            'question semantics': 'object', 
            'reasoning skills': ['object-attribute', 'exist', 'superlative'], 
            'answer types': 'binary'
        }
   }
]
```

##   File Format

1. video_train/val/test.json

   record video ids of different subsets

   ```
   [
   	VIDEO_ID
   ]
   ```

2. frames_trainval.json

   record time of the current frame in the video for visualization

   ```
   {
   	'VIDEO_ID/SEGMENT_ID/FRAME_ID': Time of the current frame in the video
   }
   ```

3. object/relationship_class.json

   record categories of objects/relationships that appear in the scene graph

   ```
   [
   	object/relationship_class,
   ]
   ```

4. attribute_class.json

   record categories of attribute that appear in the scene graph

   ```
   {
   	'color':[
   		attribute_class,	
   	],
   	'shape':[
   		attribute_class,
   	],
   }
   ```
