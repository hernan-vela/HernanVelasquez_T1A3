def delete_unit_resident(unit_residents):
    """ 
    Eliminate information of a main resident associated with a specific unit number.
    (parameters) unit_residents: load the information stored in a JSON file with all owners/tenants of the building.
    Return: Message of entry successfully deleted.
    """

    # Iteration to validate existence of entry to delete
    while True:
        unit_deletion = input(
            "Enter the number of the unit you want to vacate or 'q' to quit: ")

        # Allows user to enter 'Q' or 'q' to exit the loop
        if unit_deletion.lower() == 'q':
            return

        # Error handling if input has invalid characters (eg. % $ ^ & >, or letters)
        if not unit_deletion.isalnum():
            print(
                "Invalid input. Please enter a valid unit number or press 'q' to return to the main menu.")
            continue

        # Validates existence of key to delete and removes it
        for resident in unit_residents:
            if resident["unit"] == unit_deletion:
                unit_residents.remove(resident)
                print(f"Entry for unit {unit_deletion} has been removed.")
                return

        # Message in case that entry does not exist
        print(f"No entry found for unit {unit_deletion}. Please try again.")
