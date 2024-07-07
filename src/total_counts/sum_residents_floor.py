def sum_residents_floor(unit_residents):
    """
    Prompts the user to input a floor level and calculates the total number of residents living on that floor.
    (parameters) unit_residents: list of dictionaries containing resident information.
    Return: None
    """
    floors = ["G", "1", "2", "3", "4"]

    # Iteration to validate if floor level exist
    while True:
        floor = input(
            "\nEnter floor level to calculate the registered residents (G, 1, 2, 3, 4) or 'q' to quit: ").upper()

        # Conditional allows user to escape the programme
        if floor == 'Q':
            break

        # Error handling if floor level does not exist
        if floor not in floors:
            print(
                "Invalid entry. Please enter a valid floor level (G, 1, 2, 3, 4) or press 'q' to quit.")
            continue

        # Check all entries of unit_residents and counts residents living in floor input
        floor_residents = 0
        for entry in unit_residents:
            unit = entry["unit"]
            if (floor == "G" and unit.startswith("G")) or unit.startswith(floor):
                floor_residents += entry["num_resid"]

        # Display number of registered residents living in floor input
        print(
            f"Number of registered residents on floor {floor}: {floor_residents}")