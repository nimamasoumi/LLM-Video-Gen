import torch
from model import Model
import argparse

# Processing the arguments
parser = argparse.ArgumentParser(description='What video would you like me to make for you?')
parser.add_argument('--prompt', help='the video description')
parser.add_argument('--chunk_size', help='chunk size for GPU procesing. Choose a smaller value if your GPU RAM is limited', default=8, type=int)
args = parser.parse_args()

# Text to Video
model = Model(device="cuda", dtype=torch.float16)
prompt = args.prompt
params = {"t0": 44, "t1": 47 , "motion_field_strength_x" : 12, "motion_field_strength_y" : 12, "video_length": 32, "chunk_size": args.chunk_size}
out_path, fps = f"./text2video_{prompt.replace(' ','_')}.mp4", 8
model.process_text2video(prompt, fps = fps, path = out_path, watermark=None, **params)