from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
import time

# Llama model setup
llm = Ollama(model="llama3", stop=["<|eot_id|>"])

# To use this model, first run 'ollama pull llama3:70b' in the terminal.
# llm = Ollama(model="llama3:70b", stop=["<|eot_id|>"])

def get_model_response(user_prompt, system_prompt):
    template = """
<|begin_of_text|>
<|start_header_id|>system<|end_header_id|>
{system_prompt}
<|start_header_id|>user<|end_header_id|>
{user_prompt}
<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>
"""
    
    prompt = PromptTemplate(
        input_variables=["system_prompt", "user_prompt"],
        template=template,
    )
    
    response = llm(prompt.format(system_prompt=system_prompt, user_prompt=user_prompt))
    return response

# System prompt setup
# system_message = "You are a helpful assistant that answers questions accurately and follows instructions precisely."

# Where system prompt 
system_message = "You are a decision-making assistant. Always choose the best option strictly from the given numbered choices. Answer ONLY in the format 'Answer:X' where X is the number of the choice."


# easy prompt----------------------------------
# user_prompt = """The character is currently looking north.
# Go straight twice and turn right once
# If you go straight 1 time and turn left 1 time, where is the character looking?
# At this time, turn right and turn left are 90 degrees. And please answer in the same format as "Answer: a".

# a. the north
# b. South
# c. East
# d. the west
# e. be not looking anywhere
# """

# hard prompt----------------------------------
# user_prompt = """The character is currently looking north. 
# Go straight twice and turn right twice 
# Go straight once and turn left three times
# I made a U-turn and kept going straight.
# And then I was in the left lane at the intersection to make a left turn
# I accidentally went straight. Where is the current character looking?
# At this time, turn right and turn left are 90 degrees. And please answer in the same format as "Answer: a".

# a. the north
# b. South
# c. East
# d. the west
# e. be not looking anywhere"""


# where prompt----------------------------------
# user_prompt = """I'm a graduate student with one day left to submit my CVPR thesis. 
# The lab I'm in is on fire. 
# But my important thesis materials are in the lab and in the professor's room. 
# If I can't publish my thesis now, I have to continue my unemployed life where I can't graduate, get a job, and do nothing. 
# If I don't get this thesis, the sky will collapse, but the lab is on fire. 
# There's a wall in front of me and an emergency exit on the left 
# There is a server room on the right and a professor's room on the back. Where should I go? Answer like "Answer:1."

# 1. The front
# 2. Left
# 3. Right
# 4. The back"""

user_prompt = """My building is on fire. There is a wall in front of me from my current location and an emergency exit on the left
There is a server room on the right and a professor's room on the back. Where should I go? Answer like "Answer:1."

1. The front
2. Left
3. Right
4. The back"""

responses = []

print("Collecting 1 response from Llama...")

for i in range(1000):
    try:
        response = get_model_response(user_prompt, system_message)
        print(f"Response {i+1}: {response}")
        responses.append(response)
        
        # Short delay to reduce server load
        time.sleep(0.1)
    
    except Exception as e:
        print(f"Response {i+1} Error: {e}")
        responses.append(None)

print(f"\nTotal successful responses: {len([r for r in responses if r is not None])}")

# Save all responses to a file
with open("llama3_easy_where_1000.txt", "w", encoding="utf-8") as f:
    for i, response in enumerate(responses):
        f.write(f"Response {i+1}: {response}\n")
        f.write("-" * 50 + "\n")

print("Responses were saved to 'llama3_easy_where_1000.txt'.")
