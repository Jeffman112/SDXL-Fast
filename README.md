<p align="center">
  <img src="https://github.com/Jeffman112/SDXL-Fast/assets/123284838/20e2397a-c464-478e-a699-8271681067ba" width="300" height="300" alt="Generated Image">
</p>

# SDXL-Fast: Accelerated Text-to-Image Generation with SDXL

## Overview

SDXL-Fast is a Python script that utilizes the `StableDiffusionXLPipeline` for high-speed text-to-image generation. With astonishingly fast image generation times (around 15 seconds on my benchmark GPU, RTX 3060 Ti, and faster on higher end GPUs), you can transform text prompts into high-quality 1024x1024 images in seconds!

---

## Getting Started

1. Clone the repository to your local machine using Git:
```bash
git clone https://github.com/Jeffman112/SDXL-Fast.git
```
2. Navigate to the project directory:
```bash
cd SDXL-Fast
```
3. Install the required dependencies using pip and the provided requirements.txt file:
```bash
pip install -r requirements.txt
```

## Usage
Once you've completed the setup, you can start generating images from text prompts using SDXL-Fast. Here's how:

Run the script using the following command:
```bash
python main.py
```
Follow the on-screen instructions. The script will prompt you to enter a text prompt.

After providing the prompt, an image will be generated.

## Example Outputs
<p align="center">
  <img src="https://github.com/Jeffman112/SDXL-Fast/assets/123284838/ddf57c26-49a4-4789-ad85-357b4dab8da9" alt="dragonborn" width="300">
  <img src="https://github.com/Jeffman112/SDXL-Fast/assets/123284838/a0f6b0b8-3257-4aa1-b3c2-a4bf3b70ad35" alt="red panda" width="300">
  <img src="https://github.com/Jeffman112/SDXL-Fast/assets/123284838/73153707-892c-4222-96c7-dfd5030e8a85" alt="angel" width="300">
</p>


### Credits
This script uses the StableDiffusionXLPipeline from the Segmind organization.
The underlying models are powered by PyTorch and Hugging Face's Transformers library.

If you encounter any issues or have questions, please don't hesitate to reach out to me in the Issue Tracker.
