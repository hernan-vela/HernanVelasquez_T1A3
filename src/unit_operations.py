def display_residents(unit_residents):
    """ 
    Fetch information of building residents from a JSON file.
    (parameters) residents: load the information stored in a JSON file with all owners/tenants of the building.
    Return: List of units in the builiding with information of unit number, full name of resident, type of resident and number of people in the household.
    """
    for person in unit_residents:
        print(
            f"Unit {person['unit']}: {person['first_name']} {person['last_name']}, Status: {person['resid_type']}, Registered residents: {person['num_resid']}")


def display_unit_info(unit_residents, unit_num):
    """
    Upon user request, fetch information of a specific unit number, from a JSON file.
    (parameters) residents: residents info from JSON file.
        unit_num: input from user in the range of apartments in the building.
    Return: Unit number, full name of main resident, type of resident and number of people in the household.
    """
# unit_num = input("Enter the unit number: ") (ARGUMENT REQUESTED FROM USER IN main.py)
    for unit in unit_residents:
        if unit["unit"] == unit_num:
            print(
                f"\nUnit: {unit['unit']}\nResident: {unit['first_name']} {unit['last_name']}\nStatus: {unit['resid_type']}\nRegistered residents : {unit['num_resid']}\n")


def add_new_resident(unit_residents):
    """
    Allows user to add new resident information and stores info in a JSON file.
    (parameters) residents: list of residents registered as owner/tenat of every unit, from JSON file.
    Return: message of succesful addition.
    """
    while True:
        unit = input("Unit of new resident: ")

        if unit == 'q':
            return

        if any(non_vacant_unit["unit"] == unit for non_vacant_unit in unit_residents):
            print(
                "This unit is not vacant. Not possible to store information. Returning to main menu.")
            return

        if unit not in building_units:
            print("Unit non-existent. Try again or press 'q' to return to the main menu.")
            if unit == 'q':
                return
            else:
                continue
        else:
            break

    first_name = input("First name of owner/lessee: ")
    while not first_name.isalpha():
        print("Invalid input. Please enter a valid name with alphabetic characters only or press 'q' to return to the main menu.")
        first_name = input("First name of owner/lessee: ")
        if (first_name == 'q'):
            return

    last_name = input("Last name of owner/lessee: ")
    while not last_name.isalpha():
        print("Invalid input. Please enter a valid last name with alphabetic characters only or press 'q' to return to the main menu.")
        last_name = input("First name of owner/lessee: ")
        if (last_name == 'q'):
            return

    resid_type = input("Is this person the owner? (Yes/No): ").strip().lower()
    while resid_type not in ("yes", "no"):
        print("Invalid answer. Please enter 'Yes', 'No' or press 'q' to return to the main menu.")
        resid_type = input(
            "Is this person the owner? (Yes/No): ").strip().lower()
        if (resid_type == 'q'):
            return

    if resid_type == "yes":
        resid_type = "Owner"
    else:
        resid_type = "Tenant"

    while True:
        num_resid = input("Number of people in the household: ")

        if num_resid.lower() == 'q':
            print("Returning to the main menu.")
            return

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

    resident = {"unit": unit, "first_name": first_name,
                "last_name": last_name, "resid_type": resid_type, "num_resid": num_resid}

    unit_residents.append(resident)
    print(f"New main resident successfully added to unit {unit}.")


def delete_unit_resident(unit_residents, unit_deletion):
    """ 
    Eliminate information of a main resident associated to a specific unit number.
    (parameters) residents: load the information stored in a JSON file with all owners/tenants of the building.
                unit_num: locate the entry of the unit number information to be erased.
    Return: Message of entry successfully deleted.
    """
# unit_deletion = input("Enter the number of unit you want to vacate: ")
    while unit_deletion.isalpha() or unit_deletion.lower() == 'q':
        if unit_deletion.lower() == 'q':
            return
        print(f"Invalid input. Please enter a valid unit number or press 'q' to return to the main menu.")
        unit_deletion = input("Enter the number of unit you want to vacate: ")

    while True:
        for resident in unit_residents:
            if resident["unit"] == unit_deletion:
                unit_residents.remove(resident)
                print(f"Entry for unit {unit_deletion} has been removed.")
                return
        print(f"Unit is vacant or is an invalid unit number.")
        return


def sum_residents_floor(unit_residents, floor):
    """
    Takes the number of residents per household in the same floor and adds them up.
    (parameters) unit_residents: list of dictionaries containing resident information.
                floor: string representing the floor level for which the residents will be counted.
    Return: Total number of residents living on the same floor.
    """
    floor_residents = 0
    
    for entry in unit_residents:
        unit = entry["unit"]
        if (floor == "G" and unit.startswith("G")) or unit.startswith(floor):
            floor_residents += entry["num_resid"]
    
    return floor_residents

while True:
    floor = input("Enter floor level to calculate the registered residents (G, 1, 2, 3, 4) or 'q' to quit: ").upper()
    
    if floor == 'Q':
        break
    
    if floor not in floors:
        print("Invalid entry. Please enter a valid floor level (G, 1, 2, 3, 4) or press 'q' to quit.")
        continue
    
    total_residents = sum_residents_floor(unit_residents, floor)
    print(f"Number of registered residents on floor {floor}: {total_residents}")


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