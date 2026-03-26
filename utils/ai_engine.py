import os
import requests

API_KEY = os.getenv("GROQ_API_KEY")

def ask_estimator(user_input):

    if not API_KEY:
        raise Exception("API key missing")

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are a civil engineering estimator."},
            {"role": "user", "content": user_input}
        ]
    }

    res = requests.post(url, headers=headers, json=data)
    result = res.json()

    if "choices" not in result:
        raise Exception(result)

    return result["choices"][0]["message"]["content"]
