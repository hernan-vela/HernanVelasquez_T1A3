def add_new_resident(unit_residents, building_units):
    """
    Allows user to add new resident information and stores info in a JSON file.
    (parameters) unit_residents: list of residents registered as owner/tenat of every unit, from JSON file.
    Return: message of succesful addition.
    """

   # Iteration to ensure that unit is empty and it can take a new resident
    while True:
        unit = input("Unit of new resident: ").upper()

        # takes user out of the programme
        if unit == 'Q':
            return

        # Error handling in case the user wants to overwrite an entry
        if any(non_vacant_unit["unit"] == unit for non_vacant_unit in unit_residents):
            print(
                "\nThis unit is not vacant. Not possible to store information. Returning to main menu.")
            return

        # If user inputs a non-existent unit (e.g., 3,1416) prompts the user to try again
        if unit not in building_units:
            print("Unit non-existent. Try again or press 'q' to return to the main menu.")
            continue
        else:
            break

    # Loop to avoid invalid first names. Valid name or 'q' escapes the loop
    first_name = input("First name of owner/lessee: ")
    while not first_name.isalpha():
        print("Invalid input. Please enter a valid name with alphabetic characters only or press 'q' to return to the main menu.")
        first_name = input("First name of owner/lessee: ")
        if (first_name == 'q'):
            return

    # Loop to avoid invalid last names. Valid name or 'q' escapes the loop
    last_name = input("Last name of owner/lessee: ")
    while not last_name.isalpha():
        print("Invalid input. Please enter a valid last name with alphabetic characters only or press 'q' to return to the main menu.")
        last_name = input("First name of owner/lessee: ")
        if (last_name == 'q'):
            return

    # Loop to avoid invalid ansers. Valid yes/no or 'q' exits the loop
    resid_type = input("Is this person the owner? (Yes/No): ").strip().lower()
    while resid_type not in ("yes", "no"):
        print("Invalid answer. Please enter 'Yes', 'No' or press 'q' to return to the main menu.")
        resid_type = input(
            "Is this person the owner? (Yes/No): ").strip().lower()
        if (resid_type == 'q'):
            return

    # Condition for {Yes: Owner} or {No: Tenant}
    if resid_type == "yes":
        resid_type = "Owner"
    else:
        resid_type = "Tenant"

    # Loop to assess valid integer as number of residents in the unit
    while True:
        num_resid = input("Number of people in the household: ")

        # Takes user out of the loop
        if num_resid.lower() == 'q':
            print("Returning to the main menu.")
            return

        # Error handling for negative integers, 0 residents or invalid inputs (eg. , < = [)
        try:
            num_resid = int(num_resid)
            if num_resid < 0:
                print("Please enter a positive number.")
            elif num_resid == 0:
                print("The unit should have at least one person living in it")
            else:
                break
        except ValueError:
            print(
                "Value error. Please enter a valid number or press 'q' to return to the main menu.")

    # New entry stored with variable 'resident'
    resident = {"unit": unit, "first_name": first_name,
                "last_name": last_name, "resid_type": resid_type, "num_resid": num_resid}

    # Addition of new resident to unit_residents.json
    unit_residents.append(resident)
    print(f"New main resident successfully added to unit {unit}.")