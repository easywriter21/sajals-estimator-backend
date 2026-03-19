from utils.boq_generator import generate_boq

def calculate_cost(data):

    built_up_area = data.get("builtUpArea", 0)
    floors = data.get("floors", 1)

    total_area = built_up_area * floors

    cost_per_sqft = 1800

    total_cost = total_area * cost_per_sqft

    cement = total_area * 0.4
    sand = total_area * 0.5
    steel = total_area * 4

    boq = generate_boq(total_area)

    return {
        "total_area": total_area,
        "cement_bags": cement,
        "sand_tons": sand,
        "steel_kg": steel,
        "cost_per_sqft": cost_per_sqft,
        "estimated_cost": total_cost,
        "boq": boq
    }
