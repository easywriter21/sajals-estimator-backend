import os
import requests

API_KEY = os.getenv("GROQ_API_KEY")

def ask_estimator(user_input):

    if not API_KEY:
        raise Exception("GROQ_API_KEY not set")

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": "You are a civil engineering estimator."},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    if "choices" not in result:
        raise Exception(f"AI Error: {result}")

    return result["choices"][0]["message"]["content"]
