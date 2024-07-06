import json

def display_residents(unit_residents):
    """ 
    Fetch information of building residents from a JSON file.
    (parameters) unit_residents: load the information stored in a JSON file with all owners/tenants of the building.
    Return: List of units in the builiding with information of unit number, full name of resident, type of resident and number of people in the household.
    """

    # Display nicely information of all residents in the building
    for person in unit_residents:
        print(
            f"\nUnit {person['unit']}: {person['first_name']} {person['last_name']}, Status: {person['resid_type']}, Registered residents: {person['num_resid']}")
        

def display_unit_info(unit_residents, building_units):
    """
    Fetches and displays information of a specific unit number upon user request.
    (parameters) unit_residents: list of residents info from JSON file.
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
            print(f"Oops! Nothing found for unit {unit}")


def add_new_resident(unit_residents, building_units):
    """
    Allows user to add new resident information and stores info in a JSON file.
    (parameters) unit_residents: list of residents registered as owner/tenat of every unit, from JSON file.
    Return: message of succesful addition.
    """

   # Iteration to ensure that unit is empty and it can take a new resident
    while True:
        unit = input("Unit of new resident: ").upper()

        # takes user out of the programme
        if unit == 'Q':
            return

        # Error handling in case the user wants to overwrite an entry
        if any(non_vacant_unit["unit"] == unit for non_vacant_unit in unit_residents):
            print("\nThis unit is not vacant. Not possible to store information. Returning to main menu.")
            return

        # If user inputs a non-existent unit (e.g., 3,1416) prompts the user to try again
        if unit not in building_units:
            print("Unit non-existent. Try again or press 'q' to return to the main menu.")
            continue
        else:
            break

    # Loop to avoid invalid first names. Valid name or 'q' escapes the loop
    first_name = input("First name of owner/lessee: ")
    while not first_name.isalpha():
        print("Invalid input. Please enter a valid name with alphabetic characters only or press 'q' to return to the main menu.")
        first_name = input("First name of owner/lessee: ")
        if (first_name == 'q'):
            return

    # Loop to avoid invalid last names. Valid name or 'q' escapes the loop
    last_name = input("Last name of owner/lessee: ")
    while not last_name.isalpha():
        print("Invalid input. Please enter a valid last name with alphabetic characters only or press 'q' to return to the main menu.")
        last_name = input("First name of owner/lessee: ")
        if (last_name == 'q'):
            return

    # Loop to avoid invalid ansers. Valid yes/no or 'q' exits the loop
    resid_type = input("Is this person the owner? (Yes/No): ").strip().lower()
    while resid_type not in ("yes", "no"):
        print("Invalid answer. Please enter 'Yes', 'No' or press 'q' to return to the main menu.")
        resid_type = input(
            "Is this person the owner? (Yes/No): ").strip().lower()
        if (resid_type == 'q'):
            return

    # Condition for {Yes: Owner} or {No: Tenant}
    if resid_type == "yes":
        resid_type = "Owner"
    else:
        resid_type = "Tenant"

    # Loop to assess valid integer as number of residents in the unit
    while True:
        num_resid = input("Number of people in the household: ")

        # Takes user out of the loop 
        if num_resid.lower() == 'q':
            print("Returning to the main menu.")
            return

        # Error handling for negative integers, 0 residents or invalid inputs (eg. , < = [)
        try:
            num_resid = int(num_resid)
            if num_resid < 0:
                print("Please enter a positive number.")
            elif num_resid == 0:
                print("The unit should have at least one person living in it")
            else:
                break
        except ValueError:
            print(
                "Value error. Please enter a valid number or press 'q' to return to the main menu.")

    # New entry stored with variable 'resident'
    resident = {"unit": unit, "first_name": first_name,
                "last_name": last_name, "resid_type": resid_type, "num_resid": num_resid}

    # Addition of new resident to unit_residents.json
    unit_residents.append(resident)
    print(f"New main resident successfully added to unit {unit}.")


def delete_unit_resident(unit_residents):
    """ 
    Eliminate information of a main resident associated with a specific unit number.
    (parameters) unit_residents: load the information stored in a JSON file with all owners/tenants of the building.
    Return: Message of entry successfully deleted.
    """

    # Iteration to validate existence of entry to delete
    while True:
        unit_deletion = input("Enter the number of the unit you want to vacate or 'q' to quit: ")

        # Allows user to enter 'Q' or 'q' to exit the loop
        if unit_deletion.lower() == 'q':
            return

        # Error handling if input has invalid characters (eg. % $ ^ & >, or letters)
        if not unit_deletion.isalnum():
            print("Invalid input. Please enter a valid unit number or press 'q' to return to the main menu.")
            continue

        # Validates existence of key to delete and removes it
        for resident in unit_residents:
            if resident["unit"] == unit_deletion:
                unit_residents.remove(resident)
                print(f"Entry for unit {unit_deletion} has been removed.")
                return
        
        # Message in case that entry does not exist
        print(f"No entry found for unit {unit_deletion}. Please try again.")


def sum_residents_floor(unit_residents):
    """
    Prompts the user to input a floor level and calculates the total number of residents living on that floor.
    (parameters) unit_residents: list of dictionaries containing resident information.
    Return: None
    """
    floors = ["G", "1", "2", "3", "4"]

    # Iteration to validate if floor level exist
    while True:
        floor = input("\nEnter floor level to calculate the registered residents (G, 1, 2, 3, 4) or 'q' to quit: ").upper()
        
        # Conditional allows user to escape the programme
        if floor == 'Q':
            break
        
        # Error handling if floor level does not exist
        if floor not in floors:
            print("Invalid entry. Please enter a valid floor level (G, 1, 2, 3, 4) or press 'q' to quit.")
            continue
        
        # Check all entries of unit_residents and counts residents living in floor input
        floor_residents = 0
        for entry in unit_residents:
            unit = entry["unit"]
            if (floor == "G" and unit.startswith("G")) or unit.startswith(floor):
                floor_residents += entry["num_resid"]
        
        # Display number of registered residents living in floor input
        print(f"Number of registered residents on floor {floor}: {floor_residents}")


def total_residents_building(unit_residents):
    """
    Calculates the total number of residents in the building.
    (parameters) unit_residents: list of dictionaries containing resident information.
    Return: Total number of residents in the building.
    """

    # Initialize count of residents
    total_residents = 0
    
    # Starts count of residents adding all the entries from the unit_residents file
    for unit in unit_residents:
        total_residents += unit["num_resid"]
    # Display Total of registered residents in the building    
    print(f"\nCurrent registered residents in the building: {total_residents}")

