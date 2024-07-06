import os
from datetime import datetime
import json

unit_residents = [
    {
        "unit": "G01",
        "first_name": "Josh",
        "last_name": "Flanagan",
        "resid_type": "Owner",
        "num_resid": 7
    },
    {
        "unit": "G02",
        "first_name": "Edouard",
        "last_name": "Baxter",
        "resid_type": "Owner",
        "num_resid": 200
    },
    {
        "unit": "101",
        "first_name": "Uri",
        "last_name": "Chan",
        "resid_type": "Tenant",
        "num_resid": 100
    },
    {
        "unit": "102",
        "first_name": "Uri",
        "last_name": "Geller",
        "resid_type": "Tenant",
        "num_resid": 1
    }
]

unit_body_corp = [
    {
        "Unit": "G01",
        "Body Corporate balance": 2000
    },
    {
        "Unit": "G02",
        "Body Corporate balance": 1500
    },
    {
        "Unit": "G03",
        "Body Corporate balance": 2000
    },
    {
        "Unit": "G04",
        "Body Corporate balance": 1000
    },
    {
        "Unit": "101",
        "Body Corporate balance": 1000
    },
    {
        "Unit": "102",
        "Body Corporate balance": 1500
    },
    {
        "Unit": "103",
        "Body Corporate balance": 2500
    },
    {
        "Unit": "104",
        "Body Corporate balance": 2000
    },
    {
        "Unit": "201",
        "Body Corporate balance": 5000
    },
    {
        "Unit": "202",
        "Body Corporate balance": 1000
    },
    {
        "Unit": "203",
        "Body Corporate balance": 2500
    },
    {
        "Unit": "204",
        "Body Corporate balance": 2000
    },
    {
        "Unit": "301",
        "Body Corporate balance": 2000
    },
    {
        "Unit": "302",
        "Body Corporate balance": 4000
    },
    {
        "Unit": "303",
        "Body Corporate balance": 10200
    },
    {
        "Unit": "304",
        "Body Corporate balance": 10500
    }
]

building_units = ["G01", "G02", "G03", "G04", "101", "102", "103", "104", "201",
                  "202", "203", "204", "301", "302", "303", "304", "401", "402", "403", "404"]


floors = ["G", "1", "2", "3", "4"]


def bodyCorp_unit_balance(unit_body_corp, building_units):
    """
    User fetches information of the current balance of a unit by entering the unit number.
    (parameters) unit_body_corp: List of entries with accumulation of payments per unit in a JSON file.
    Return: None
    """
    
    while True:
        unit = input("Enter unit to see the current Body Corporate balance or 'q' to quit: ").upper()

        if unit == 'Q':
            break

        if unit not in building_units:
            print("Invalid entry. Please enter a valid unit number or press 'q' to quit.")
            continue

        balance = None
        for entry in unit_body_corp:
            if entry["Unit"] == unit:
                balance = entry["Body Corporate balance"]
                break
        
        if balance is not None:
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\nDate: {current_datetime}\nUnit: {unit}\nBC balance: {balance}\n")
        else:
            print(f"No balance information found for unit {unit}.")

bodyCorp_unit_balance(unit_body_corp, building_units)