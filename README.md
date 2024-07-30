# Video Generation using Large Language Models (LLMs)
Do you enjoy running text-to-video generation codes on Google Colab as much as I do? 

Try [this Notebook](https://github.com/nimamasoumi/blob/main/llm-video-gen.ipynb) in Colab and explore the enabling possibilities.

Well, this repository provides a Jupyter Notebook and inference files of [Text2Video-Zero](https://arxiv.org/abs/2303.13439) runnable on Google Colab.

The official sources codes are provided in the [Text2Video GitHub](https://github.com/Picsart-AI-Research/Text2Video-Zero). 

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
<li>The method generates certain poses better than other e.g. horse galloping or running toward the camera angle.</li>
<li>The generation of complex poses usually fail e.g. an animal slowly turns the head from left to right.</li>
<li>Generated videos of human are not realistic e.g. I tried Elon Musk and it did not go well. </li>
<li>Results are usually a close-up and focused to the described subjects, and the background is missing. </li>
<li>The videos containing flows of water can be very similar to an animated paining.</li>
<li>In general, the videos are like animated paining, regardless of the generation prompt. </li>
</ol>

