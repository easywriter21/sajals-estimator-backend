from utils.live_cost import get_live_costs

def generate_estimate(text: str):

    area = 1200
    floors = 2
    total_area = area * floors

    rcc_volume = total_area * 0.15
    steel_kg = total_area * 4
    cement_bags = rcc_volume * 8

    sand_tons = total_area * 0.05
    aggregate_tons = total_area * 0.04

    costs = get_live_costs()

    material_cost = (
        cement_bags * costs["cement_per_bag"] +
        steel_kg * costs["steel_per_kg"] +
        sand_tons * costs["sand_per_ton"] +
        aggregate_tons * costs["aggregate_per_ton"]
    )

    labour_cost = material_cost * 0.4
    total_cost = material_cost + labour_cost

    duration_days = int(total_area / 40)

    return {
        "project": text,
        "area": total_area,

        "cement_bags": int(cement_bags),
        "steel_kg": int(steel_kg),
        "sand_tons": int(sand_tons),
        "aggregate_tons": int(aggregate_tons),

        "material_cost": int(material_cost),
        "labour_cost": int(labour_cost),
        "total_cost": int(total_cost),

        "duration_days": duration_days,
        "rates": costs
    }
