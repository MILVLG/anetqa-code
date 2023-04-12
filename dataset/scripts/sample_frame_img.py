import json
import os

frames_trainval = json.load(open("../meta/frames_trainval.json"))

for frame_ids in frames_trainval:
    ids=frame_ids.split("/")
    video_id = ids[0]
    segment_id = ids[1]
    frame_id = ids[2]
    vid_path = f"../videos/{video_id}.mp4"
    if not os.path.exists(vid_path):
        vid_path = f"../videos/{video_id}.mkv"
    segment_path = f"../frames/{video_id}/{segment_path}"
    if not os.path.exists(segment_path):
        os.makedirs(segment_path)
    os.system(' '.join(('ffmpeg', '-loglevel', 'panic', '-ss', str(frames_trainval[frame_ids]), '-i', vid_path, '-vframes', '1', '-vf','scale=720:-1', os.path.join(segment_path, str(frame_id).zfill(2)+'.jpg'))))