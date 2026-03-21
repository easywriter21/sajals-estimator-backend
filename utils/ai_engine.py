import os
import requests

# Get API key securely from Render environment
API_KEY = os.getenv("GROQ_API_KEY")


def ask_estimator(user_input):

    # Safety check
    if not API_KEY:
        raise Exception("GROQ_API_KEY not set in environment variables")

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # 🔥 PROFESSIONAL CIVIL ENGINEERING PROMPT
    system_prompt = """
You are Estimator, an expert Civil Engineer, Quantity Surveyor, and Construction Cost Estimator.

STRICT RULES:

1. Follow Indian construction standards (IS codes)
2. Use realistic engineering values:
   - Cement: ~0.4 bags per sq ft
   - Steel: 3–5 kg per sq ft
   - Cost: ₹1600–₹2500 per sq ft

3. Always structure output EXACTLY in this format:

PROJECT SUMMARY:
- Built-up area
- Floors
- Building type

QUANTITY CALCULATIONS:
- RCC volume (m³)
- Brickwork (m³)
- Plaster area (m²)

MATERIAL REQUIREMENTS:
- Cement (bags)
- Sand (m³)
- Aggregate (m³)
- Steel (kg)

BOQ TABLE:
Item | Unit | Quantity | Rate | Cost

TOTAL COST:
₹ value

COST PER SQ FT:
₹ value

TIMELINE:
Estimated construction duration

IMPORTANT:
- Use correct engineering formulas
- Use correct units (m³, kg, sq ft)
- Avoid unrealistic/random numbers
- Keep output clean and structured
"""

    # 🔥 CURRENT WORKING MODEL
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    }

    # API request
    response = requests.post(url, headers=headers, json=data)

    # Debug (optional - keep during development)
    print("STATUS:", response.status_code)
    print("RAW RESPONSE:", response.text)

    # Convert response
    try:
        result = response.json()
    except Exception:
        raise Exception("Invalid JSON response from AI API")

    # Handle API errors cleanly
    if "choices" not in result:
        raise Exception(f"AI ERROR: {result}")

    # Extract AI message
    try:
        output = result["choices"][0]["message"]["content"]
    except Exception:
        raise Exception("Unexpected AI response format")

    return output
