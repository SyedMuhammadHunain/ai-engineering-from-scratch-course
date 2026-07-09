from google import genai
from dotenv import load_dotenv
import os
import requests

load_dotenv()

# Google SDK Request
client_sdk = genai.Client();

response_of_sdk = client_sdk.interactions.create(
    model='gemini-flash-lite-latest',
    input='Write a short poem about the beauty of nature.',
);

# Raw HTTP Request
url="https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent"
headers = {
    "Content-Type": "application/json",
    "X-goog-api-key": os.getenv("GEMINI_API_KEY"),
}
json_data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": "Write a short poem about the beauty of nature."
                    }
                ]
            }
        ]
    }
response_of_rawhttp = requests.post(
    url,
    headers=headers,
    json=json_data
);

# Response Comparison
print(response_of_sdk);
print("\n\n\n");
print(response_of_rawhttp.json());


