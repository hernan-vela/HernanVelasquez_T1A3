def total_residents_building(unit_residents):
    """
    Calculates the total number of residents in the building.
    (parameters) unit_residents: list of dictionaries containing resident information.
    Return: Total number of residents in the building.
    """

    # Initialize count of residents
    total_residents = 0

    # Starts count of residents adding all the entries from the unit_residents file
    for unit in unit_residents:
        total_residents += unit["num_resid"]
    # Display Total of registered residents in the building
    print(f"\nCurrent registered residents in the building: {total_residents}")