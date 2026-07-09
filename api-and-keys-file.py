# from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

# client = genai.Client();

# response = client.interactions.create(
#     model='gemini-flash-lite-latest',
#     input='Write a short poem about the beauty of nature.',
# );

# print(response.output_text);

import requests

url="https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

response = requests.post(
    url,
    headers={
        "Content-Type": "application/json",
        "X-goog-api-key": os.getenv(),
    },
    json={
        "contents": [
            {
                "parts": [
                    {
                        "text": "Explain how AI works in a few words"
                    }
                ]
            }
        ]
    },
);

print(response.json());
