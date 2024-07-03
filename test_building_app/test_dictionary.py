unit_residents = [
    {
        "unit": "G01",
        "occupied": True,
        "first_name": "Josh",
        "last_name": "Flanagan",
        "resid_type": "Owner",
        "num_resid": 5
    },
    {
        "unit": "102",
        "occupied": True,
        "first_name": "Edouard",
        "last_name": "Baxter",
        "resid_type": "Owner",
        "num_resid": 3  
    },
    {
        "unit": "G03",
        "occupied": True,
        "first_name": "Uri",
        "last_name": "Chan",
        "resid_type": "tenant",
        "num_resid": 10
    },
    {
        "unit": "G04",
        "occupied": True,
        "first_name": "Uri",
        "last_name": "Geller",
        "resid_type": "Tenant",
        "num_resid": 1
    }
]



def sum_residents_building(residents):
    """
    Sum the total of number of residents currently living in the building.
    (parameter) residents: (CHECK, CHECK)
    Return: Total number of people living in the building.
    """
    try:
        count_residents = 0

        for num_resid in count_residents:
            count_residents += num_resid["num_resid"]
            print(f"Total number of people living in the building: {count_residents_residents}")

    total_residents()