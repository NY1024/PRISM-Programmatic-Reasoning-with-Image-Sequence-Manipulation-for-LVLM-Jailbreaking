import requests
import json


API_KEY = ""
API_URL = ""

def dalle3_generate_image(prompt, size="1024x1024", quality="standard", filename="1.png"):
    payload = {
        "model": "volcengine/high_aes_general_v30l_zt2i",
        "prompt": prompt,
        "n": 1,
        "size": size,
        "quality": quality
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        image_url = data["data"][0]["url"]
        
       
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(image_response.content)
            print(f"图像已保存为 {filename}")
        else:
            raise Exception(f"下载图像失败，状态码: {image_response.status_code}, 信息: {image_response.text}")
    else:
        raise Exception(f"图像生成失败，状态码: {response.status_code}, 信息: {response.text}")


prompt = "A futuristic city skyline at sunset"
dalle3_generate_image(prompt)
