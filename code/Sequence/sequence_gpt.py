import json
import os
import base64
from openai import OpenAI

client = OpenAI(api_key="secret key")

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

experiments = [
    {
        "model": "gpt-4.1",
        "task": "masking",
        "input_folder": "/home/jaey00ns/PythonCodes/sequence_new/sequence_masking",
        "prompt": "Look at the given image. the upper 4 images show a sequence. and the third image is missing. you have to choose between image a and b below. which one is the missing image? \n Answer :",
        "output_file": "experiment/gpt41_m.json"
    },
    {
        "model": "gpt-4.1",
        "task": "validation",
        "input_folder": "/home/jaey00ns/PythonCodes/sequence_new/sequence_validation",
        "prompt": "Look at the given image. Which direction did I turn, left or right?\n Answer :",
        "output_file": "experiment/gpt41_v.json"
    },
    {
        "model": "gpt-5.2",
        "task": "masking",
        "input_folder": "/home/jaey00ns/PythonCodes/sequence_new/sequence_masking",
        "prompt": "Look at the given image. the upper 4 images show a sequence. and the third image is missing. you have to choose between image a and b below. which one is the missing image? \n Answer :",
        "output_file": "experiment/gpt52_m.json"
    },
    {
        "model": "gpt-4.1",
        "task": "validation",
        "input_folder": "/home/jaey00ns/PythonCodes/sequence_new/sequence_validation",
        "prompt": "Look at the given image. Which direction did I turn, left or right? \n Answer :",
        "output_file": "experiment/gpt41_v.json"
    }
]


os.makedirs("experiment", exist_ok=True)

for exp_idx, exp in enumerate(experiments, 1):
    print(f"\n{'='*60}")
    print(f"{exp_idx}/4: {exp['model']} - {exp['task']}")
    print(f"{'='*60}")
    
    MODEL = exp["model"]
    input_folder = exp["input_folder"]
    prompt = exp["prompt"]
    output_file = exp["output_file"]
    results = []
    
    print(f"{MODEL} benchmark started...")
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, filename)
            print(f"Processing: {filename}")
            
            try:
                base64_image = encode_image(image_path)
                
                response = client.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {
                            "role": "user", 
                            "content": [
                                {
                                    "type": "text", 
                                    "text": prompt
                                },
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/png;base64,{base64_image}"
                                    }
                                }
                            ]
                        }
                    ]
                )
                
                generated_text = response.choices[0].message.content.strip()
                results.append({
                    "image_name": filename,
                    "output": generated_text
                })
                
                print(f"Result: {generated_text}")
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                results.append({
                    "image_name": filename,
                    "output": f"Error: {e}"
                })
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\nProcessing completed! Results saved to {output_file}")
    print(f"Total processed images: {len(results)}")

