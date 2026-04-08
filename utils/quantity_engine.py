def calculate_quantities(area, floors):
    total = area * floors

    return {
        "cement": total * 0.4,
        "steel": total * 3.5,
        "sand": total * 0.015,
        "aggregate": total * 0.025
    }
