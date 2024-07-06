import os

unit_residents = [
    {
        "unit": "G01",
        "first_name": "Josh",
        "last_name": "Flanagan",
        "resid_type": "Owner",
        "num_resid": 5
    },
    {
        "unit": "G02",
        "first_name": "Edouard",
        "last_name": "Baxter",
        "resid_type": "Owner",
        "num_resid": 3
    },
    {
        "unit": "101",
        "first_name": "Uri",
        "last_name": "Chan",
        "resid_type": "Tenant",
        "num_resid": 7
    },
    {
        "unit": "102",
        "first_name": "Uri",
        "last_name": "Geller",
        "resid_type": "Tenant",
        "num_resid": 1
    }
]

building_units = ["G01", "G02", "G03", "G04", "101", "102", "103", "104", "201",
                  "202", "203", "204", "301", "302", "303", "304", "401", "402", "403", "404"]


floors = ["G", "1", "2", "3", "4"]


def total_residents_building(unit_residents):
    """
    Calculates the total number of residents in the building.
    (parameters) unit_residents: list of dictionaries containing resident information.
    Return: Total number of residents in the building.
    """
    total_residents = 0
    
    for unit in unit_residents:
        total_residents += unit["num_resid"]
    
    return total_residents

total_residents = total_residents_building(unit_residents)
print(f"Current registered residents in the building: {total_residents}")


