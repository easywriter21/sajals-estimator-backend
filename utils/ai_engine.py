import os
import requests

API_KEY = os.getenv("GROQ_API_KEY")

def ask_estimator(user_input):

    if not API_KEY:
        raise Exception("Missing GROQ_API_KEY")

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    system_prompt = """
You are Estimator, an expert Civil Engineer and Quantity Surveyor.

Perform:
1. Analyze building details
2. Calculate quantities (RCC, PCC, brickwork etc.)
3. Estimate materials (cement, sand, steel)
4. Generate BOQ table
5. Provide total cost (Indian rates)
6. Cost per sq ft
7. Timeline

Explain clearly for students.
"""

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    return result["choices"][0]["message"]["content"]
