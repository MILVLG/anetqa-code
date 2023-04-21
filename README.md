# Code for ANetQA baselines

This repository contains code for our baselines, namely HCRN, ClipBERT, and All-in-one, which is migrated from their original implementations to fit our data structure.

## Dataset Preparation 

see [dataset](https://github.com/MILVLG/anetqa-code/tree/main/dataset) for details.

## Model Setup, Training, and Testing

see the [HCRN](https://github.com/MILVLG/anetqa-code/tree/main/hcrn), [ClipBERT](https://github.com/MILVLG/anetqa-code/tree/main/ClipBERT), and [All-in-one](https://github.com/MILVLG/anetqa-code/tree/main/all-in-one) folders for details.

## Results

The above models deliver the following results on `val` and `test-dev` set.

|         | HCRN  | ClipBERT | All-in-one |
| ------- | ----- | -------- | --------------- |
| val      | 41.69 | 44.34    | 45.44      |
| test-dev | 41.18 | 44.00    | 44.57      |

|            | val set | test-dev set |                |
| ---------- | ------- | ------------ | -------------- |
| HCRN       | 41.69   | 41.18        | [checkpoint]() |
| ClipBERT   | 44.34   | 44.00        | [checkpoint]() |
| All-in-one | 45.44   | 44.57        | [checkpoint]() |

## License

This project is licensed under the Apache License 2.0.

## Citation
If you use ANetQA in your research, we appreciate it if you cite our paper in the following.

```
@inproceedings{yu2023anetqa,
title={ANetQA: A Large-scale Benchmark for Fine-grained Compositional Reasoning over Untrimmed Videos},
   author={Yu, Zhou and Zheng, Lixiang and Zhao, Zhou and Wu, Fei and Fan, Jianping and Ren, Kui and Yu, Jun},
   booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
   year={2023}
}
```

