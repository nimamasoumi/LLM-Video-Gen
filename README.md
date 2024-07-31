<a target="_blank" href="https://colab.research.google.com/github/nimamasoumi/LLM-Video-Gen/blob/main/llm-video-gen.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

# Video Generation using Large Language Models
Do you enjoy running text-to-video generation codes on Google Colab as much as I do? 

Try [this Notebook](https://github.com/nimamasoumi/LLM-Video-Gen/blob/main/llm-video-gen.ipynb) in Colab and explore the enabling possibilities.

This repository provides a Jupyter Notebook and inference files of [Text2Video-Zero](https://arxiv.org/abs/2303.13439), which are executable on Google Colab.

The official source codes are provided in the [Text2Video GitHub](https://github.com/Picsart-AI-Research/Text2Video-Zero). 

Below are the examples that I created using the source codes:

<table class="center" style="width:70%; height:70%">
<tr>
  <td><img src="examples/gif/text2video_A_gray-brown_fox_roaring_and_turning_head.gif" raw=true></td>
  <td><img src="examples/gif/text2video_A_gray_fox_roaring.gif" raw=true></td>
  <td><img src="examples/gif/text2video_depth_control_oil painting roaring gray fox, a high-quality, detailed, and professional photo.gif" raw=true></td>
  <td><img src="examples/gif/text2video_edge_guidance_oil painting of a fox, a high-quality, detailed, and professional photo.gif" raw=true></td>
</tr>
</table>

Following example was created using Hugging Face page of the official repository:

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/PAIR/Text2Video-Zero)

<p>
<img src="examples/gif/text2video_HuggingFace.gif" raw=true style="width:40%; height:40%">
</p>

## What I learned using this text-to-video method?
<ol>
<li>Certain poses are better illustrated e.g. horse galloping or moving animals toward the camera.</li>
<li>The generation of complex poses usually fails, e.g. an animal slowly turns the head from left to right.</li>
<li>Generated videos of humans are not realistic, e.g. I tried Elon Musk and it did not go well. </li>
<li>Results are usually a close-up and focused to the described subjects, and the background is missing. </li>
<li>The videos containing flows of water can be very similar to an animated paining.</li>
<li>In general, the videos are like animated painting, regardless of the generation prompt. </li>
</ol>

