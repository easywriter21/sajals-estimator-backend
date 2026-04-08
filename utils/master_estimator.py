from utils.quantity_engine import calculate_quantities
from utils.cost_engine import calculate_cost
from utils.constraint_engine import apply_budget, calculate_duration

def master_estimate(area, floors, rates, budget=None, time_limit=None):

    qty = calculate_quantities(area, floors)
    costs = calculate_cost(qty, rates)

    costs = apply_budget(costs, budget)

    material_cost = sum(costs.values())
    labour_cost = area * floors * rates["labour"]

    duration = calculate_duration(area, floors, 12)

    total_cost = material_cost + labour_cost

    return {
        "Area": area,
        "Floors": floors,
        "Material Cost": material_cost,
        "Labour Cost": labour_cost,
        "Total Cost": total_cost,
        "Estimated Days": duration
    }
