import torch
import decord
from decord import cpu, gpu
from tqdm import tqdm
import json
import os
import random
import numpy as np
import pickle


def sample_frames(num_frames, vlen, sample='rand', fix_start=None):
    acc_samples = min(num_frames, vlen)
    intervals = np.linspace(start=0, stop=vlen, num=acc_samples + 1).astype(int)
    ranges = []
    for idx, interv in enumerate(intervals[:-1]):
        ranges.append((interv, intervals[idx + 1] - 1))
    if sample == 'rand':
        frame_idxs = [random.choice(range(x[0], x[1])) for x in ranges]
    elif fix_start is not None:
        frame_idxs = [x[0] + fix_start for x in ranges]
    elif sample == 'uniform':
        frame_idxs = [(x[0] + x[1]) // 2 for x in ranges]
    else:
        raise NotImplementedError

    return frame_idxs

video_list_train = json.load(open("video_train.json"))
video_list_val = json.load(open("video_val.json"))
video_list_test = json.load(open("video_test.json"))
for video_id in tqdm(video_list_train):
    if os.path.exists(f"videos/{video_id}.mp4"):
        video_path = f"videos/{video_id}.mp4"
    else:
        video_path = f"videos/{video_id}.mkv"
    video_reader = decord.VideoReader(video_path, width=512, height=512)
    decord.bridge.set_bridge('torch')
    vlen=len(video_reader)
    for i in range(1,10):
        frame_idxs = sample_frames(3, vlen, sample="rand")
        frames = video_reader.get_batch(frame_idxs).byte()
        frames = frames.permute(0, 3, 1, 2)
        frame_ids[f"{video_id}_{i}"]=frame_idxs
        pickle.dump(frames,open(f"allinone_data/images/rand_new/{video_id}_{i}","wb"))

for video_id in tqdm(video_list_val+video_list_test):
    if os.path.exists(f"videos/{video_id}.mp4"):
        video_path = f"videos/{video_id}.mp4"
    else:
        video_path = f"videos/{video_id}.mkv"
    video_reader = decord.VideoReader(video_path, width=512, height=512, num_threads=1)
    decord.bridge.set_bridge('torch')
    vlen=len(video_reader)
    frame_idxs = sample_frames(3, vlen, sample="uniform")
    frames = video_reader.get_batch(frame_idxs).byte()
    frames = frames.permute(0, 3, 1, 2)
    pickle.dump(frames,open(f"clipbert/images/uniform/{video_id}","wb"))
