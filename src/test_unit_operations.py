# def display_residents(residents):
#     """ 
#     Fetch information of owner/tenant from a JSON file.
#     (parameters) residents: (CHECK, CHECK).
#     Return: None
#     """
#     try:
#         for person in residents:
#             print(f"Unit {person['unit']}, {person['first_name']} {person['last_name']}, status: {person['resid_type']}, Residents/unit: {person['num_resid']}")
#     except KeyError as e:
#         print(f"Error displaying information of residents: Missing key {e}")
#     except Exception as e:
#         print(f"An expected error occurred: {e}")

def add_new_resident(residents):
    """
    Allows user to add new resident information and stores information in a JSON file.
    (parameters) residents: (CHECK, CHECK)
    Return: 
    """

    try:
        unit = input("Unit of new resident: ")
        first_name = input("First name of owner/lessee: ")
        last_name = input("Last name of owner/lessee: ")
        resid_type = input("Is this person the owner?(Yes/No): ")
        num_resid = int(input("Number of people in the household: "))   

        residents = {"unit": unit, "first_name": first_name, "last_name": last_name, "resid_type": resid_type, "num_resid": num_resid}
        residents.append()

    except Exception as e:
        print("An expected error has occurred", e)
        return []
    # add_new_resident()