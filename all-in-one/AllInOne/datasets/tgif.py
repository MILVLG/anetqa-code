import numpy as np
from .video_base_dataset import BaseDataset, read_frames_gif
import os
import json
import pandas as pd
import cv2
import random
import torch

# 2022.1.28 read gif is too slow, may be need to speedup by convert gif -> video
# https://stackify.dev/833655-python-convert-gif-to-videomp4


class TGIFDataset(BaseDataset):
    def __init__(self, *args, split="", **kwargs):
        assert split in ["train", "val", "test"]
        self.split = split
        self.metadata = None
        self.ans_lab_dict = None
        if split == "train":
            names = ["tgif_train"]
        elif split == "val":
            names = ["tgif_val"]
        elif split == "test":
            names = ["tgif_test"]

        super().__init__(
            *args,
            **kwargs,
            names=names,
            text_column_name="questions",
            remove_duplicate=False,
        )
        # self.num_frames = 4
        self._load_metadata()
        self.video_len=json.load(open("meta_data/tgif/video_len.json"))
        self.video_fps=json.load(open("meta_data/tgif/video_fps.json"))

    def _load_metadata(self):
        metadata_dir = './meta_data/tgif'
        split_files = {
            'train': 'data_train.jsonl',
            'val': 'data_val.jsonl',  # frameqa_val.jsonl
            'test': 'data_test.jsonl'
        }
        target_split_fp = split_files[self.split]
        answer_fp = os.path.join(metadata_dir, 'anetqa_trainval_ans2label.json')
        # answer_fp = os.path.join(metadata_dir, 'msrvtt_qa_ans2label.json')
        with open(answer_fp, 'r') as JSON:
            self.ans_lab_dict = json.load(JSON)
        # path_or_buf=os.path.join(metadata_dir, target_split_fp)
        metadata = pd.read_json(os.path.join(metadata_dir, target_split_fp), lines=True)
        self.metadata = metadata

    def _get_video_path(self, sample):
        return os.path.join(self.data_dir, 'gifs', sample['gif_name']) + '.gif', sample['gif_name'] + '.gif'

    def get_raw_video(self, sample):
        # abs_fp, rel_fp = self._get_video_path(sample)
        # imgs, idxs, vlen = read_frames_gif(abs_fp, self.num_frames, mode=self.split)
        video_name=sample['gif_name']
        if self.split == 'train':
            fps = self.video_fps[video_name]
            vlen = self.video_len[video_name]
            seconds = vlen//fps
            if video_name in ["v_leJM3mgm_gU","v_xQxT2_meU50","v_Oyi0X-rwUg8","v_PN99KIY7jRY","v_Y8WY_c3onSY","v_sOUNe30PXY4","v__MYAaRrTeMQ","v_tVIY6uyH3aA","v__zAfwnDt4VE","v_zq621OgpFFk", "v_HHDMFrN7vFs","v_HHDMFrN7vFs","v_BcflqWdlBjI","v_gU81ZXdYh7o","v_eQc-8npRq18","v_u10c6Nx4K0A","v_DXOKFXlx84M","v_Ht2gV7oaqbo","v_EzX0FZI6pCg","v_h8cXVe6N6Oc","v_gCx-ucvPhDY","v_Fdjw9ld-hbA","v_GWJw2jR2mTY","v_taHfD8TFfX4",
                                "v_0ERgbWePjWk","v_-vqefJDOxkw","v_OHwE8aA90IE","v_C4V6fqELvPY","v_fJ7gcHxxJMM","v_2UJ4wqJt_Y8","v_1aNOjjLWjxc","v_CAW0CEuyvZo","v_HbXNXmCRFh4","v_AWryNQMbcd8","v_cWrOETjOOTc","v_7wBrvMGZROQ","v_OSndW3d2XxU","v_arfBwR8qgPw","v_wott7JRSkOk"]:
                frame_idxs=[0,fps-1,fps]
            else:
                intervals = np.linspace(start=0, stop=seconds, num=self.num_frames + 1).astype(int)
                ranges = []
                for idx, interv in enumerate(intervals[:-1]):
                    ranges.append((interv, intervals[idx + 1] - 1))
                frame_idxs = [random.choice(range(x[0], x[1]))*fps for x in ranges]
            imgs= np.zeros((3,512,512,3))
            for idx,frame_id in enumerate(frame_idxs):
                img = cv2.imread(f"meta_data/imgs/{video_name}_{frame_id}.jpg")
                imgs[idx]=img
            imgs = torch.tensor(imgs)
            imgs = imgs.permute(0, 3, 1, 2).type(torch.FloatTensor)
        else:
            imgs= np.zeros((3,512,512,3))
            for i in range(3):
                img = cv2.imread(f"meta_data/val_imgs/{video_name}_{i}.jpg")
                imgs[i]=img
            imgs = torch.tensor(imgs)
            imgs = imgs.permute(0, 3, 1, 2).type(torch.FloatTensor)
        
        if imgs is None:
            raise Exception("Invalid img!")
        else:
            return imgs

    def get_text(self, sample):
        text = sample['question']
        encoding = self.tokenizer(
            text,
            padding="max_length",
            truncation=True,
            max_length=self.max_text_len,
            return_special_tokens_mask=True,
        )
        return (text, encoding)

    def get_answer_label(self, sample):
        text = sample['answer']
        ans_total_len = len(self.ans_lab_dict) + 1  # one additional class
        try:
            ans_label = self.ans_lab_dict[text]  #
        except KeyError:
            ans_label = -100  # ignore classes
            # ans_label = 1500 # other classes
        scores = np.zeros(ans_total_len).astype(int)
        scores[ans_label] = 1
        return text, ans_label, scores
        # return text, ans_label_vector, scores

    def __getitem__(self, index):
        sample = self.metadata.iloc[index]
        image_tensor = self.get_video(sample)
        text = self.get_text(sample)
        # index, question_index = self.index_mapper[index]
        qid = index
        ques_id = sample["key"]
        # if self.split != "test":
        #     answers, labels, scores = self.get_answer_label(sample)
        # else:
        #     answers = list()
        #     labels = list()
        #     scores = list()
        answers, labels, scores = self.get_answer_label(sample)
        

        return {
            "image": image_tensor,
            "text": text,
            "vqa_answer": answers,
            "vqa_labels": labels,
            "vqa_scores": scores,
            "qid": qid,
            "ques_id":ques_id
        }

    def __len__(self):
        return len(self.metadata)