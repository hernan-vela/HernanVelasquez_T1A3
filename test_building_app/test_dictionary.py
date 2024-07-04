unit_residents = [
    {
        "unit": "G01",
        "occupied": True,
        "first_name": "Josh",
        "last_name": "Flanagan",
        "resid_type": "Owner",
        "num_resid": 5
    },
    {
        "unit": "G02",
        "occupied": True,
        "first_name": "Edouard",
        "last_name": "Baxter",
        "resid_type": "Owner",
        "num_resid": 3  
    },
    {
        "unit": "101",
        "occupied": True,
        "first_name": "Uri",
        "last_name": "Chan",
        "resid_type": "tenant",
        "num_resid": 10
    },
    {
        "unit": "102",
        "occupied": True,
        "first_name": "Uri",
        "last_name": "Geller",
        "resid_type": "Tenant",
        "num_resid": 1
    }
]

unit_num = input("Enter the unit number: ")

for unit in unit_residents:
    if unit["unit"] == unit_num:
        print(unit)






