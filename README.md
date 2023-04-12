# Code for ANetQA baselines

This repository contains code for our baselines hcrn, clipbert, and all-in-one. For all three baselines, we used their code for the FrameQA questions in the TGIF-QA benchmark, then adjusted to fit our data structure. You can download ANetQA from our [website](https://milvlg.github.io/anetqa).

## Prepare dataset

see [dataset](https://github.com/MILVLG/anetqa-code/tree/main/dataset)

## Models

see [hcrn](https://github.com/MILVLG/anetqa-code/tree/main/hcrn), [clipbert](https://github.com/MILVLG/anetqa-code/tree/main/ClipBERT), [all-in-one](https://github.com/MILVLG/anetqa-code/tree/main/all-in-one)

## Results

**val acc**

|         | hcrn  | ClipBERT | all-in-one-base |
| ------- | ----- | -------- | --------------- |
| overall | 41.69 | 44.34    | 45.44           |

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](https://github.com/MILVLG/anetqa-code/blob/main/LICENSE) file for details.

## Citing ANetQA 

If you use ANetQA in your research or wish to refer to the baseline results, please use the following BibTeX entry.

```
@inproceedings{yu2023anetqa,
title={ANetQA: A Large-scale Benchmark for Fine-grained Compositional Reasoning over Untrimmed Videos},
author={Yu, Zhou and Zheng, Lixiang and Zhao, Zhou and Wu, Fei and Fan, Jianping and Ren, Kui and Yu, Jun},
booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
year={2023}
}
```

