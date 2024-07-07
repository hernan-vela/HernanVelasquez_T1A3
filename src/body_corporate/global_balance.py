import json

def global_balance(unit_body_corp):
    """
    User fetches information of current total balance of Body Corporate
    (parameters) unit_body_corp: List of entries with accumulation of payments per unit in a JSON file.
    Return: Total balance of Body Corporate YTD
    """

    # Intializes total count for balance
    total_bc_balance = 0

    # Iterates to add up every Bodi Corporate balance of the building
    for unit in unit_body_corp:
        balance = unit["Body Corporate balance"]
        total_bc_balance += balance

    # Display the total Body Corporate balance
    print(
        f"\nYear to Date, the global Body Corporate balance is: ${total_bc_balance}")
