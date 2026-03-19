def generate_boq(area):

    return [

        {
            "item": "Earthwork Excavation",
            "unit": "m3",
            "quantity": area * 0.03,
            "rate": 250
        },

        {
            "item": "PCC",
            "unit": "m3",
            "quantity": area * 0.01,
            "rate": 5500
        },

        {
            "item": "RCC Concrete",
            "unit": "m3",
            "quantity": area * 0.02,
            "rate": 7500
        },

        {
            "item": "Brickwork",
            "unit": "m3",
            "quantity": area * 0.05,
            "rate": 6500
        }

    ]
