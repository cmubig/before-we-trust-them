import os
import time

from google import genai


client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

if not os.environ.get("GOOGLE_API_KEY"):
    raise RuntimeError(
        "GOOGLE_API_KEY is not set. Export it first, e.g. `export GOOGLE_API_KEY=...`"
    )


# prompt = """The character is currently looking north.
# Go straight twice and turn right once
# If you go straight 1 time and turn left 1 time, where is the character looking?
# At this time, turn right and turn left are 90 degrees. And please answer in the same format as "Answer: a".

# a. the north
# b. South
# c. East
# d. the west
# e. be not looking anywhere"""

# where prompt----------------------------------
# prompt = """I'm a graduate student with one day left to submit my CVPR thesis. 
# The lab I'm in is on fire. 
# But my important thesis materials are in the lab and in the professor's room. 
# If I can't publish my thesis now, I have to continue my unemployed life where I can't graduate, get a job, and do nothing. 
# If I don't get this thesis, the sky will collapse, but the lab is on fire. 
# There's a wall in front of me and an emergency exit on the left 
# There is a server room on the right and a professor's room on the back. Where should I go? Answer like "Answer:1." with the reason explained.

# 1. The front
# 2. Left
# 3. Right
# 4. The back"""

prompt = """My building is on fire. There is a wall in front of me from my current location and an emergency exit on the left
There is a server room on the right and a professor's room on the back. Where should I go? Answer like "Answer:1." with the reason explained.

1. The front
2. Left
3. Right
4. The back"""

responses = []

for i in range(1):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        print(f"Response {i+1}: {response.text}")
        responses.append(response.text)
        
        # Short delay to avoid API rate limits
        time.sleep(0.1)
        
    except Exception as e:
        print(f"Response {i+1} Error: {e}")
        responses.append(None)

# Result analysis
print(f"\nTotal successful responses: {len([r for r in responses if r is not None])}")

# Save all responses to a file (optional)
with open("Reason_gemini2_where_easy_9.txt", "w", encoding="utf-8") as f:
    for i, response in enumerate(responses):
        f.write(f"Response {i+1}: {response}\n")
        f.write("-" * 50 + "\n")
