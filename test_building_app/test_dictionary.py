import os

unit_residents = [
    {
        "unit": "G01",
        "first_name": "Josh",
        "last_name": "Flanagan",
        "resid_type": "Owner",
        "num_resid": 5
    },
    {
        "unit": "G02",
        "first_name": "Edouard",
        "last_name": "Baxter",
        "resid_type": "Owner",
        "num_resid": 3
    },
    {
        "unit": "101",
        "first_name": "Uri",
        "last_name": "Chan",
        "resid_type": "Tenant",
        "num_resid": 10
    },
    {
        "unit": "102",
        "first_name": "Uri",
        "last_name": "Geller",
        "resid_type": "Tenant",
        "num_resid": 1
    }
]


building_units = ["G01", "G02", "G03", "G04", "101", "102", "103", "104", "201",
                  "202", "203", "204", "301", "302", "303", "304", "401", "402", "403", "404"]



unit_deletion = input("Enter the number of unit you want to vacate: ")

def delete_unit_resident(unit_residents, unit_deletion):
    """ 
    Eliminate information of a main resident associated to a specific unit number.
    (parameters) residents: load the information stored in a JSON file with all owners/tenants of the building.
                unit_num: locate the entry of the unit number information to be erased.
    Return: Message of entry successfully deleted.
    """

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

delete_unit_resident(unit_residents, unit_deletion)

