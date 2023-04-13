# Dataset

## Videos and QA pairs

Download the videos and dataset from [here](https://milvlg.github.io/anetqa/#Dataset), and unzip the files to form the folder structure as follows:

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

After the data preparation, you can use the following script to visualize the scene graph on selected frames.

```
python script/sample_frame_img.py
```

## Scene Graph Files

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

## QA Files

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

## Meta information Files

`video_train.json`, `video_val.json`, and `video_test.json` contain the list of their corresponding video ids. 

```
[
     VIDEO_ID,
     ...
]
```

`frame_trainval.json` contains the selected frame in scene graphs

```
{
     'VIDEO_ID/SEGMENT_ID/FRAME_ID':TIME,
     ...
}
```

`object_class.json` and `relationship_class.json` contain the lists of object and relationship classes.

```
[
     OBJECT_CLASS (RELATIONSHIP_CLASS),
     ...
]
```

`attribute_class.json` contains a hierarchy of attribute classes

```
{
     'color':
     [
          attribute_class,
          ...
     ],
     'shape':
     [
          attribute_class,
          ...
     ],
}
```
