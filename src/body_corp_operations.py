from datetime import datetime
import json


def bodyCorp_unit_balance(unit_body_corp, unit):
    """
    User fetches information of current balance of a unit, by entering the unit number
    (parameters) unit_body_corp: List of entries with accumulation of payments per unit in a JSON file.
                unit: Unit number input by the user when executing the function.
    Return: Date/time, unit number and current body corporate balance of unit.
    """
    for entry in unit_body_corp:
        if entry["Unit"] == unit:
            return entry["Body Corporate balance"]
    return None


while True:
    unit = input(
        "Enter unit to see the current Body Corporate balance or 'q' to quit: ").upper()

    if unit == 'Q':
        break

    if unit not in building_units:
        print("Invalid entry. Please enter a valid unit number or press 'q' to quit.")
        continue

    balance = bodyCorp_unit_balance(unit_body_corp, unit)
    if balance is not None:
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(
            f"\nDate: {current_datetime}\nUnit: {unit}\nBC balance: {balance}\n")
    else:
        print(f"No balance information found for unit {unit}.")


def global_building_balance(unit_body_corp):
    """
    User fetches information of current total balance of Body Corporate
    (parameters) unit_body_corp: List of entries with accumulation of payments per unit in a JSON file.
    Return: Total balance of Body Corporate YTD
    """
    total_BC_balance = 0

    for unit in unit_body_corp:
        balance = unit["Body Corporate balance"]
        total_BC_balance += balance
    print(
        f"Year to Date, the global Body Corporate balance is: ${total_BC_balance}")
