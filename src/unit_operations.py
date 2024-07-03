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

        # if first_name != None:
        #     occupied = True
        # else:
        #     occupied = False

        last_name = input("Last name of owner/lessee: ")
        resid_type = input("Is this person the owner?(Yes/No): ")
        resid_type = resid_type.lower()
        if resid_type == "yes":
            resid_type = "Owner"
        else:
            resid_type = "Tenant"
        # print(resid_type) # DO I NEED TO PRINT THIS LINE?

        num_resid = int(input("Number of people in the household: "))        

        residents = {"unit": unit, "first_name": first_name, "last_name": last_name, "resid_type": resid_type, "num_resid": num_resid}
        residents.append()

    except ValueError:
        print("Error: Invalid input. Number of people must be an integer.")
    except Exception as e:
        print(f"An expected error occurred: {e}")

def residents_floor(residents, num_resid, floor):
    """
    Takes the number of residents per household in the same floor and add them up.
    (parameters) residents: (CHECK, CHECK), floor: level G, 1) SHOULD I INCLUDE MORE LEVELS????????
    Return: Total of residents living in the same floor.
    """
    try:
        for num_resid in 