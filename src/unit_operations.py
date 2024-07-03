def display_residents(residents):
    """ 
    Fetch information of owner/tenant from a JSON file.
    (parameters) residents: (CHECK, CHECK).
    Return: None
    """
    try:
        for person in residents:
            print(f"Unit {person['unit']}, {person['first_name']} {person['last_name']}, status: {person['resid_type']}, Residents/unit: {person['num_resid']}")
    except KeyError as e:
        print(f"Error displaying information of residents: Missing key {e}")
    except Exception as e:
        print(f"An expected error occurred: {e}")

def add_new_resident(residents):
    """
    Allows user to add new resident information and stores info in a JSON file.
    (parameters) residents: (CHECK, CHECK)
    Return: message of succesful addition.
    """
    try:
        unit = input("Unit of new resident: ")
        first_name = input("First name of owner/lessee: ")

        if first_name != None:
            occupied = True
        else:
            occupied = False

        last_name = input("Last name of owner/lessee: ")
        resid_type = input("Is this person the owner?(Yes/No): ")
        
        resid_type = resid_type.lower()
        if resid_type == "yes":
            resid_type = "Owner"
        elif resid_type == "no":
            resid_type == "Tenant"

        
        num_resid = int(input("Number of people in the household: "))        
        
        residents = {"unit": unit, "first_name": first_name, "last_name": last_name, "resid_type": resid_type, "num_resid": num_resid}
        residents.append()

    except ValueError:
        print("Error: Invalid input. Number of people must be an integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


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
                print(f"Number of residents in the {floor} is {floor_residents}")
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
            print(f"Total number of people living in the building: {total_residents}")




