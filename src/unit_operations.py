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
    Return: print unit, full name of main resident, type of resident and number of people in the household.
    """
    try:

        # unit_num = input("Enter the unit number: ") (ARGUMENT REQUESTED FROM USER IN main.py)
        for unit in unit_residents:
            if unit["unit"] == unit_num:
                print(f"\nUnit: {unit['unit']}\nResident: {unit['first_name']} {unit['last_name']}\nStatus: {unit['resid_type']}\nRegistered residents : {unit['num_resid']}")
    # except KeyError as e:
    #     print(f"Unit number does not exist or unit is vacant. Missing key {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def add_new_resident(unit_residents):
    """
    Allows user to add new resident information and stores info in a JSON file.
    (parameters) residents: list of residents registered as owner/tenat of every unit, from JSON file.
    Return: message of succesful addition.
    """

    unit = input("Unit of new resident: ")
    while unit not in building_units:  # LINK THIS LINE TO 'building_units.json'
        print("Unit non-existent. Try again or press 'q' to return to the main menu.")
        unit = input("Unit of new resident: ")
        if (unit == 'q'):
            return

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
            print("Value error. Please enter a valid number or press 'q' to return to the main menu.")


    resident = {"unit": unit, "first_name": first_name,
                "last_name": last_name, "resid_type": resid_type, "num_resid": num_resid}

    unit_residents.append(resident)
    print(f"New main resident successfully added to unit {unit}.")

def sum_residents_floor(residents, floor):
    """
    Takes the number of residents per household in the same floor and add them up.
    (parameters) residents: (CHECK, CHECK), floor: level G, 1) SHOULD I INCLUDE MORE LEVELS????????
    Return: Total of residents living in the same floor.
    """
    try:
        floor_residents = 0

        # Iterate through unit numbers a sum residents in the same level
        for unit in unit_residents:
            if unit["unit"].starstwith(str(floor)):
                floor_residents += unit["num_resid"]
                print(
                    f"Number of residents in the {floor} is {floor_residents}")
    except ValueError as e:
        print(f"Incorrect/inexistent floor number. Enter a valid floor number")
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")


def total_residents(residents):
    """
    Sum the total of number of residents currently living in the building.
    (parameter) residents: (CHECK, CHECK)
    Return: Total number of people living in the building.
    """
    try:
        total_residents = 0

        for num_resid in unit_residents:
            total_residents += num_resid["num_resid"]
            print(
                f"Total number of people living in the building: {total_residents}")
