def generate_boq(area):

    return [
        {"item": "Excavation", "unit": "m3", "quantity": area*0.03, "rate": 250, "cost": area*0.03*250},
        {"item": "PCC", "unit": "m3", "quantity": area*0.01, "rate": 5500, "cost": area*0.01*5500},
        {"item": "RCC", "unit": "m3", "quantity": area*0.02, "rate": 7500, "cost": area*0.02*7500},
        {"item": "Brickwork", "unit": "m3", "quantity": area*0.05, "rate": 6500, "cost": area*0.05*6500}
    ]
