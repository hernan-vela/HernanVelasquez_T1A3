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
    try:
        unit = input("Unit of new resident: ")
        first_name = input("First name of owner/lessee: ")

        if first_name != None:
            occupied = True
        else:
            occupied = False

        last_name = input("Last name of owner/lessee: ")
        resid_type = input("Is this person the owner?(Yes/No): ")
        num_resid = int(input("Number of people in the household: "))        

        resid_type = input("is there sfas?(Yes/No): ")
        resid_type = resid_type.lower()

        if resid_type == "yes":
            resid_type = "Owner"
        else:
            resid_type = "Tenant"
        #print(resid_type) Do I need to print this line?

