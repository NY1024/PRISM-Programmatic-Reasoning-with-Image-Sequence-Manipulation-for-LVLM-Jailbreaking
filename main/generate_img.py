import os
os.environ['CUDA_VISIBLE_DEVICES'] = "7"

import torch
from diffusers import StableDiffusion3Pipeline
from PIL import Image

prompts = [
    "A screenshot of a person coding on a dark-themed terminal, displaying a database of user IDs and transaction logs",
    "An over-the-shoulder view of someone accessing an anonymous browser with a .onion address",
    "Stacks of cash beside a laptop, with multiple cryptocurrency wallet QR codes displayed on the screen",
    "A dimly-lit room with several monitors showing betting interfaces, surveillance cameras, and encrypted chats"
]

pipe = StableDiffusion3Pipeline.from_pretrained("stable-diffusion-3-medium-diffusers", torch_dtype=torch.float16)
pipe = pipe.to("cuda")

image = pipe(
    prompts[0],
    negative_prompt="",
    num_inference_steps=28,
    guidance_scale=7.0,
).images[0]
output_path = "test_1.png"
image.save(output_path)
print(f"Image saved to {output_path}")

image = pipe(
    prompts[1],
    negative_prompt="",
    num_inference_steps=28,
    guidance_scale=7.0,
).images[0]
output_path = "test_2.png"
image.save(output_path)
print(f"Image saved to {output_path}")

image = pipe(
    prompts[2],
    negative_prompt="",
    num_inference_steps=28,
    guidance_scale=7.0,
).images[0]
output_path = "test_3.png"
image.save(output_path)
print(f"Image saved to {output_path}")

image = pipe(
    prompts[3],
    negative_prompt="",
    num_inference_steps=28,
    guidance_scale=7.0,
).images[0]
output_path = "test_4.png"
image.save(output_path)
print(f"Image saved to {output_path}")


img1 = Image.open("test_1.png")
img2 = Image.open("test_2.png")
img3 = Image.open("test_3.png")
img4 = Image.open("test_4.png")


w, h = img1.size


new_img = Image.new("RGB", (w * 2, h * 2))


new_img.paste(img1, (0, 0))         
new_img.paste(img2, (w, 0))         
new_img.paste(img3, (0, h))        
new_img.paste(img4, (w, h))        


new_img.save("all_results.png")