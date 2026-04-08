def apply_budget(costs, budget):
    total = sum(costs.values())

    if budget and total > budget:
        factor = budget / total
        costs = {k: v * factor for k, v in costs.items()}

    return costs


def calculate_duration(area, floors, labour_rate):
    total = area * floors
    return int(total / labour_rate)
