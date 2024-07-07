from datetime import datetime


def body_corp_unit_balance(unit_body_corp, building_units):
    """
    User fetches information of the current balance of a unit by entering the unit number.
    (parameters) unit_body_corp: List of entries with accumulation of payments per unit in a JSON file.
                building_units: List of all possible units in the building (JSON file)
    Return: Date, time, unit number and body corporate balance
    """
    # Iteration to match user input of unit number to its respective body corporate balance
    while True:
        unit = input(
            "\nEnter unit to see the current Body Corporate balance or 'q' to quit: ").upper()

        # Allows user to escape the loop typing 'Q' or 'q'
        if unit == 'Q':
            break

        # Check existence unit number in the building
        if unit not in building_units:
            print("\nInvalid entry. Please enter a valid unit number or press 'q' to quit.")
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
            print(f"\nNo balance information found for unit {unit}.")