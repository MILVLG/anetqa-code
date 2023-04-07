# Code for ANetQA baselines

This repository contains code for our baselines HCRN, ClipBERT, and all-in-one. For all three baselines, we used their code for the FrameQA questions in the TGIF-QA benchmark, then adjusted to fit our data structure. You can download ANetQA from our [website](https://milvlg.github.io/anetqa).

## results

| val acc | hcrn  | ClipBERT | all-in-one-base |
| ------- | ----- | -------- | --------------- |
| overall | 41.69 | 44.34    | 45.44           |

## Data

### Videos

- Download ActivityNet videos [here](http://activity-net.org/)
- Download our scene graph from our [website](https://milvlg.github.io/anetqa/)
- Download our Question-Answer pairs from our [website](https://milvlg.github.io/anetqa/)
- Download frame list from [here]()
- Download video list from [here]() (hcrn may use it)

### Scene Graph Format

```json
{...
     "v_onFddYAkyyc":{
         "objects":{...
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
         ...},
         "attributes":{...
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
         ...},
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
         ...},
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
        ...]
     }
...}
```

**Note: attributes have different formats depending on the singular or plural forms of objects.**

### ANetQA Format

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

  