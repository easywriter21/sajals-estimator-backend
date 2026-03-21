from utils.boq_generator import generate_boq

def calculate_cost(data):

    # Get input (with defaults)
    built_up_area = data.get("builtUpArea", 1200)
    floors = data.get("floors", 2)

    # Total built area
    total_area = built_up_area * floors

    # 💰 Cost estimation (Indian standard)
    cost_per_sqft = 1800  # can vary 1600–2500
    total_cost = total_area * cost_per_sqft

    # 🧱 Material estimation (realistic thumb rules)
    cement_bags = total_area * 0.4      # bags
    steel_kg = total_area * 4           # kg
    sand_m3 = total_area * 0.03         # cubic meter
    aggregate_m3 = total_area * 0.06    # cubic meter

    # Generate BOQ
    boq = generate_boq(total_area)

    return {
        "total_area_sqft": total_area,
        "cement_bags": round(cement_bags),
        "steel_kg": round(steel_kg),
        "sand_m3": round(sand_m3, 2),
        "aggregate_m3": round(aggregate_m3, 2),
        "cost_per_sqft": cost_per_sqft,
        "estimated_cost": total_cost,
        "boq": boq
    }
