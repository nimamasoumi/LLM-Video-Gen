import torch
from model import Model
import argparse

# Processing the arguments
parser = argparse.ArgumentParser(description='What video would you like me to make for you?')
parser.add_argument('--prompt', help='the video description')
parser.add_argument('--chunk_size', help='chunk size for GPU procesing. Choose a smaller value if your GPU RAM is limited', default=8, type=int)
args = parser.parse_args()

# Video to video, pose control
model = Model(device="cuda", dtype=torch.float16)
prompt = args.prompt
motion_path = '__assets__/canny_videos_mp4/fox.mp4'
out_path = f"./text2video_pose_guidance_{prompt.replace(' ','_')}.mp4"
model.process_controlnet_pose(motion_path, prompt=prompt, chunk_size=args.chunk_size, save_path=out_path, watermark=None)
