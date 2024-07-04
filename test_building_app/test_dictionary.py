# unit_residents = [
#     {
#         "unit": "G01",
#         "first_name": "Josh",
#         "last_name": "Flanagan",
#         "resid_type": "Owner",
#         "num_resid": 5
#     },
#     {
#         "unit": "G02",
#         "first_name": "Edouard",
#         "last_name": "Baxter",
#         "resid_type": "Owner",
#         "num_resid": 3  
#     },
#     {
#         "unit": "101",
#         "first_name": "Uri",
#         "last_name": "Chan",
#         "resid_type": "Tenant",
#         "num_resid": 10
#     },
#     {
#         "unit": "102",
#         "first_name": "Uri",
#         "last_name": "Geller",
#         "resid_type": "Tenant",
#         "num_resid": 1
#     }
# ]


# # def add_new_resident(unit_residents):
# #     """
# #     Allows user to add new resident information and stores info in a JSON file.
# #     (parameters) residents: (CHECK, CHECK)
# #     Return: message of succesful addition.
# #     """
# #     try:
# #         unit = input("Unit of new resident: ")
# #         first_name = input("First name of owner/lessee: ")
# #         last_name = input("Last name of owner/lessee: ")
# #         resid_type = input("Is this person the owner?(Yes/No): ")
        
# #         resid_type = resid_type.lower()
# #         if resid_type == "yes":
# #             resid_type = "Owner"
# #         elif resid_type == "no":
# #             resid_type == "Tenant"

        
# #         num_resid = int(input("Number of people in the household: "))        
        
# #         resident = {"unit": unit, "first_name": first_name, "last_name": last_name, "resid_type": resid_type, "num_resid": num_resid}
# #         unit_residents.append(resident)
# #         print("Resident added successfully.")

# #     except ValueError:
# #         print("Error: Invalid input. Number of people must be an integer.")
# #     except Exception as e:
# #         print(f"An unexpected error occurred: {e}")

# # add_new_resident(unit_residents)


# # # def display_residents(unit_residents):
# # #     """ 
# # #     Fetch information of building residents from a JSON file.
# # #     (parameters) residents: (CHECK, CHECK).
# # #     Return: List of units in the builiding with information of unit number, full name of resident, type of resident and 
# # #     number of people in the household.
# # #     """
# # #     try:
# # #         for person in unit_residents:
# # #             print(f"Unit {person['unit']}, {person['first_name']} {person['last_name']}, status: {person['resid_type']}, Residents/unit: {person['num_resid']}")
# # #     except KeyError as e:
# # #         print(f"Error displaying information of residents: Missing key {e}")
# # #     except Exception as e:
# # #         print(f"An expected error occurred: {e}")


# # # display_residents(unit_residents)



# def add_new_resident(residents):
#     """
#     Allows user to add new resident information and stores info in a JSON file.
#     (parameters) residents: list of residents registered as owner/tenat of every unit, from JSON file.
#     Return: message of succesful addition.
#     """
#     building_units = ["G01", "G02", "G03", "G04", "101", "102", "103", "104", "201", "202", "203", "204", "301", "302", "303", "304", "401", "402", "403", "404"]

#     try:
#         unit = input("Unit of new resident: ")

#         while unit not in building_units: # LINK THIS LINE TO 'building_units.json'
#             print("Unit non-existent. Try again!")

#         first_name = input("First name of owner/lessee: ")
#         last_name = input("Last name of owner/lessee: ")


while True:
    resid_type = input("Is this person the owner?(Yes/No): ").strip().lower()

    if resid_type in ["yes", "y"]:
        resid_type = "Owner"
        break
    elif resid_type in ["no", "n"]:
        resid_type = "Tenant"
        break
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")