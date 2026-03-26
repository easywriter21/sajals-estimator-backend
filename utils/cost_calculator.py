from utils.boq_generator import generate_boq

def calculate_cost(data):

    area = data.get("builtUpArea", 1200)
    floors = data.get("floors", 2)

    budget = data.get("budget")
    duration = data.get("duration")

    total_area = area * floors

    base_cost = 1800

    # 🔥 Constraint logic
    if budget:
        cost_per_sqft = budget / total_area
    else:
        cost_per_sqft = base_cost

    total_cost = total_area * cost_per_sqft

    cement = total_area * 0.4
    steel = total_area * 4

    if duration:
        labour = "High Speed Work"
    else:
        duration = total_area / 50
        labour = "Normal Work"

    return {
        "total_area": total_area,
        "cost_per_sqft": round(cost_per_sqft),
        "estimated_cost": round(total_cost),
        "cement_bags": round(cement),
        "steel_kg": round(steel),
        "duration_days": round(duration),
        "labour_type": labour,
        "boq": generate_boq(total_area)
    }
