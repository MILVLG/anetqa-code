import torch
import decord
from decord import cpu
from tqdm import tqdm
import json
import os
import random
import numpy as np
import cv2

short_videos=[  "v_leJM3mgm_gU","v_xQxT2_meU50","v_Oyi0X-rwUg8","v_PN99KIY7jRY","v_Y8WY_c3onSY","v_sOUNe30PXY4","v__MYAaRrTeMQ",
                "v_tVIY6uyH3aA","v__zAfwnDt4VE","v_zq621OgpFFk","v_HHDMFrN7vFs","v_HHDMFrN7vFs","v_BcflqWdlBjI","v_gU81ZXdYh7o",
                "v_eQc-8npRq18","v_u10c6Nx4K0A","v_DXOKFXlx84M","v_Ht2gV7oaqbo","v_EzX0FZI6pCg","v_h8cXVe6N6Oc","v_gCx-ucvPhDY",
                "v_Fdjw9ld-hbA","v_GWJw2jR2mTY","v_taHfD8TFfX4","v_0ERgbWePjWk","v_-vqefJDOxkw","v_OHwE8aA90IE","v_C4V6fqELvPY",
                "v_fJ7gcHxxJMM","v_2UJ4wqJt_Y8","v_1aNOjjLWjxc","v_CAW0CEuyvZo","v_HbXNXmCRFh4","v_AWryNQMbcd8","v_cWrOETjOOTc",
                "v_7wBrvMGZROQ","v_OSndW3d2XxU","v_arfBwR8qgPw","v_wott7JRSkOk"]
for video_id in short_videos:
    if os.path.exists(f"videos/{video_id}.mp4"):
        video_path = f"videos/{video_id}.mp4"
    else:
        video_path = f"videos/{video_id}.mkv"
    vr = decord.VideoReader(video_path, width=512, height=512, ctx=cpu(0))
    frames_num = len(vr)
    fps=int(vr.get_avg_fps())
    frame_ids = np.linspace(0,frames_num-1,8).astype(int)
    for i in frame_ids:
        frame=vr[i].asnumpy()
        cv2.imwrite(f"imgs/{video_id}_{i}.jpg",frame)


video_list_train = json.load(open("../video_train.json"))
video_list_val = json.load(open("../video_val.json"))
video_list_test = json.load(open("../video_test.json"))

for video_id in tqdm(video_list_train):
    if os.path.exists(f"videos/{video_id}.mp4"):
        video_path = f"videos/{video_id}.mp4"
    else:
        video_path = f"videos/{video_id}.mkv"
    vr = decord.VideoReader(video_path, width=512, height=512, ctx=cpu(0))
    frames_num = len(vr)
    fps=int(vr.get_avg_fps())
    seconds = frames_num//fps
    frames_num = seconds*fps
    for i in range(0,frames_num,fps):
        frame=vr[i].asnumpy()
        cv2.imwrite(f"imgs/{video_id}_{i}.jpg",frame)

for video_id in tqdm(video_list_val+video_list_test):
    if os.path.exists(f"videos/{video_id}.mp4"):
        video_path = f"videos/{video_id}.mp4"
    else:
        video_path = f"videos/{video_id}.mkv"
    vr = decord.VideoReader(video_path, width=512, height=512, ctx=cpu(0))
    vlen = len(vr)
    intervals = np.linspace(start=0, stop=vlen, num=4).astype(int)
    ranges = []
    for idx, interv in enumerate(intervals[:-1]):
        ranges.append((interv, intervals[idx + 1] - 1))
    frame_idxs = [(x[0] + x[1]) // 2 for x in ranges]
    for idx,i in enumerate(frame_idxs):
        frame=vr[i].asnumpy()
        cv2.imwrite(f"imgs/{video_id}_{idx}.jpg",frame)
