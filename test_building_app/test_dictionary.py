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
        "num_resid": 10
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


def display_residents(unit_residents):
    """ 
    Fetch information of building residents from a JSON file.
    (parameters) residents: load the information stored in a JSON file with all owner/tenant of the building
    Return: List of units in the builiding with information of unit number, full name of resident, type of resident and 
    number of people in the household.
    """
    try:
        for person in unit_residents:
            print(
                f"Unit {person['unit']}, {person['first_name']} {person['last_name']}, status: {person['resid_type']}, Residents/unit: {person['num_resid']}")
    except KeyError as e:
        print(f"Error displaying information of residents: Missing key {e}")
    except Exception as e:
        print(f"An expected error occurred: {e}")

display_residents(unit_residents)
