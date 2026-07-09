from google import genai
from dotenv import load_dotenv
import os
import requests

load_dotenv()

def sdk_function():
    """Call Gemini via the Google GenAI SDK."""
    try:
        client_sdk = genai.Client()
        response = client_sdk.interactions.create(
            model='gemini-flash-lite-latest',
            input='Write a short poem about the beauty of nature.',
        )
        return response
    except Exception as e:
        return e

def rawhttp_function():
    """Call Gemini via raw HTTP POST."""
    try:
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent"
        headers = {
            "Content-Type": "application/json",
            "X-goog-api-key": os.getenv("GEMINI_API_KEY"),
        }
        json_data = {
            "contents": [
                {
                    "parts": [
                        {"text": "Write a short poem about the beauty of nature."}
                    ]
                }
            ]
        }
        response = requests.post(url, headers=headers, json=json_data)
        return response
    except Exception as e:
        return e

def main():
    sdk_resp = sdk_function()
    raw_resp = rawhttp_function()

    print("--- SDK Result ---")
    if isinstance(sdk_resp, Exception):
        print("SDK error:", str(sdk_resp))
    else:
        # Tokens
        try:
            print("Total output tokens (SDK):", sdk_resp.usage.total_output_tokens)
        except Exception as e:
            print("Failed to get SDK token info:", e)
        # Body
        try:
            print("Generated text (SDK):")
            print(sdk_resp.output_text)
        except Exception as e:
            print("Failed to get SDK output text:", e)

    print("\n--- Raw HTTP Result ---")
    if isinstance(raw_resp, Exception):
        print("Raw HTTP error:", str(raw_resp))
    else:
        try:
            data = raw_resp.json()
            print("Total output tokens (Raw HTTP):", data["usageMetadata"]["totalTokenCount"])
            print("Generated text (Raw HTTP):")
            print(data["candidates"][0]["content"]["parts"][0]["text"])
        except Exception as e:
            print("Failed to parse Raw HTTP response:", e)

if __name__ == "__main__":
    main()
