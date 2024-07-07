import json


def display_unit_info(unit_residents, building_units):
    """
    Fetches and displays information of a specific unit number upon user request.
    (parameters) unit_residents: list of residents info from JSON file.
                building_units: JSON file with all units in the building
    Return: Unit number, full name of main resident, type of resident and number of people in the household.
    """
    # Iteration through all occupied units in the building
    while True:
        unit = input("Enter the unit number or press 'q' to quit: ").upper()

        # Takes the user out of the loop
        if unit == 'Q':
            break

        # Error handling if user inputs an invalid unit number
        if unit not in building_units:
            print("Invalid entry. Please enter a valid unit number or press 'q' to quit.")
            continue

        # Matches user input with data in the file
        for entry in unit_residents:
            if entry["unit"] == unit:
                print(
                    f"\nUnit: {entry['unit']}\nResident: {entry['first_name']} {entry['last_name']}\nStatus: {entry['resid_type']}\nRegistered residents: {entry['num_resid']}\n")
                break
        else:
            print(
                f"Oops! No owner/lessee information recorded for unit {unit}")