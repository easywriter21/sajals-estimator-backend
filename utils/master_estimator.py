import re
from utils.ai_engine import generate_estimate

def extract_area(text):
    match = re.search(r'(\d{3,5})\s*sq\s*ft', text.lower())
    return int(match.group(1)) if match else 1200


def apply_constraints(result, budget=None, duration=None):

    if budget:
        result["total_cost"] = int(budget)
        result["material_cost"] = int(budget * 0.65)
        result["labour_cost"] = int(budget * 0.35)

    if duration:
        factor = result["duration_days"] / duration
        result["duration_days"] = duration
        result["total_cost"] = int(result["total_cost"] * factor * 1.1)

    return result


def master_estimate(text, budget=None, duration=None):

    area = extract_area(text)
    result = generate_estimate(f"{area} sq ft building")

    return apply_constraints(result, budget, duration)
