def calculate_cost(qty, rates):
    return {
        "cement": qty["cement"] * rates["cement"],
        "steel": qty["steel"] * rates["steel"],
        "sand": qty["sand"] * rates["sand"],
        "aggregate": qty["aggregate"] * rates["aggregate"]
    }
