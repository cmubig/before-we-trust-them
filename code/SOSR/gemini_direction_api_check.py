import os

from google import genai


client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

if not os.environ.get("GOOGLE_API_KEY"):
    raise RuntimeError(
        "GOOGLE_API_KEY is not set. Export it first, e.g. `export GOOGLE_API_KEY=...`"
    )

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="There's a character facing north. He turns three times in place. Which direction is the character facing?"
)
print(response.text)