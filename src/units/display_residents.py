import json


def display_residents(unit_residents):
    """ 
    Fetch information of building residents from a JSON file.
    (parameters) unit_residents: load the information stored in a JSON 
    file with all owners/tenants of the building.
    Return: List of units in the builiding with information of unit 
    number, full name of resident, type of resident and number of 
    people in the household.
    """

    # Display nicely information of all residents in the building
    for person in unit_residents:
        print(f"\nUnit {person['unit']}: {person['first_name']} {person['last_name']}, Status: {person['resid_type']}, Registered residents: {person['num_resid']}")