import json
import os
from google import genai
from google.genai import types

client = genai.Client(api_key="secret key")

experiments = [
    {
        "model": "gemini-3-flash-preview",
        "task": "masking",
        "input_folder": "/home/jaey00ns/PythonCodes/sequence_new/sequence_masking",
        "prompt": "Look at the given image. the upper 4 images show a sequence. and the third image is missing. you have to choose between image a and b below. which one is the missing image? Answer :",
        "output_file": "experiment/gemini3_m.json"
    },
    {
        "model": "gemini-3-flash-preview",
        "task": "validation",
        "input_folder": "/home/jaey00ns/PythonCodes/sequence_new/sequence_validation",
        "prompt": "Look at the given image. Which direction did I turn, left or right? Answer :",
        "output_file": "experiment/gemini3_v.json"
    }
]

os.makedirs("experiment", exist_ok=True)

for exp_idx, exp in enumerate(experiments, 1):
    print(f"\n{'='*60}")
    print(f"{exp_idx}/2: {exp['model']} - {exp['task']}")
    print(f"{'='*60}")
    
    model_name = exp["model"]
    input_folder = exp["input_folder"]
    prompt = exp["prompt"]
    output_file = exp["output_file"]
    results = []
    
    print(f"{model_name} benchmark started...")
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, filename)
            print(f"Processing: {filename}")
            
            try:
                with open(image_path, 'rb') as f:
                    image_bytes = f.read()
                
                if filename.lower().endswith('.png'):
                    mime_type = 'image/png'
                elif filename.lower().endswith(('.jpg', '.jpeg')):
                    mime_type = 'image/jpeg'
                else:
                    mime_type = 'image/png'  
                
                response = client.models.generate_content(
                    model=model_name,
                    contents=[
                        types.Part.from_bytes(
                            data=image_bytes,
                            mime_type=mime_type,
                        ),
                        prompt
                    ]
                )
                
                generated_text = response.text.strip()
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
