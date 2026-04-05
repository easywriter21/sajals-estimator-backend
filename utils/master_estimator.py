def master_estimate(text: str, prices: dict):

    # Dummy calculation logic (replace later with advanced AI)
    area = 1200  # assume for now or extract from text

    cement_cost = 400 * prices["cement"]
    steel_cost = 2 * prices["steel"]
    sand_cost = 100 * prices["sand"]
    aggregate_cost = 120 * prices["aggregate"]
    labour_cost = 50 * prices["labour"]

    total_cost = cement_cost + steel_cost + sand_cost + aggregate_cost + labour_cost

    return {
        "input": text,
        "cement_cost": cement_cost,
        "steel_cost": steel_cost,
        "sand_cost": sand_cost,
        "aggregate_cost": aggregate_cost,
        "labour_cost": labour_cost,
        "total_cost": total_cost
    }
