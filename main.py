import torch
from PIL import Image
import io
import os
from diffusers import StableDiffusionXLPipeline
from diffusers.utils import load_image
import datetime

pipe = StableDiffusionXLPipeline.from_pretrained("segmind/SSD-1B", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.to("cuda")
while True:
    prompt = input("Prompt: ")
    image = pipe(prompt=prompt).images[0]

    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"output_{timestamp}.jpg"

    with io.BytesIO() as output_bytes:
        image.save(output_bytes, format="JPEG")
        image_data = output_bytes.getvalue()

    with open(filename, "wb") as file:
        file.write(image_data)