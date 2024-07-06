from datetime import datetime
import json


def bodyCorp_unit_balance(unit_body_corp, building_units):
    """
    User fetches information of the current balance of a unit by entering the unit number.
    (parameters) unit_body_corp: List of entries with accumulation of payments per unit in a JSON file.
                building_units: List of all possible units in the building (JSON file)
    Return: Date, time, unit number and body corporate balance
    """
    # Iteration to match user input of unit number to its respective body corporate balance
    while True:
        unit = input(
            "Enter unit to see the current Body Corporate balance or 'q' to quit: ").upper()

        # Allows user to escape the loop typing 'Q' or 'q'
        if unit == 'Q':
            break

        # Check existence unit number in the building
        if unit not in building_units:
            print("Invalid entry. Please enter a valid unit number or press 'q' to quit.")
            continue

        # Finds and stores as 'balance' the 'Body Corporate balance' correspondent to unit number
        balance = None
        for entry in unit_body_corp:
            if entry["Unit"] == unit:
                balance = entry["Body Corporate balance"]
                break

        # If 'balance' exists prints its value, otherwise prints 'No balance info...'
        if balance is not None:
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(
                f"\nDate: {current_datetime}\nUnit: {unit}\nBC balance: {balance}\n")
        else:
            print(f"No balance information found for unit {unit}.")


def global_balance(unit_body_corp):
    """
    User fetches information of current total balance of Body Corporate
    (parameters) unit_body_corp: List of entries with accumulation of payments per unit in a JSON file.
    Return: Total balance of Body Corporate YTD
    """

    # Intializes total count for balance
    total_BC_balance = 0

    # Iterates to add up every Bodi Corporate balance of the building
    for unit in unit_body_corp:
        balance = unit["Body Corporate balance"]
        total_BC_balance += balance

    # Display the total Body Corporate balance
    print(
        f"Year to Date, the global Body Corporate balance is: ${total_BC_balance}")
