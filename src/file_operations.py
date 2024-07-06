import json


def load_unit_residents(file_path):
    """
    Fetch and read information of residents from JSON file.
    (parameters) file_path: path to the JSON file.
    Return: List of residents or empty list in case of error.
    """
    try:

        # Opens and reads JSON file of unit_residents
        with open(file_path, 'r') as file:
            unit_residents = json.load(file)
        return unit_residents
    
    # Manage error if file is missing
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist")
        return []
    
    # Mange any other unexpected error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def save_residents(file_path, unit_residents):
    """
    Save information of residents in a JSON file.
    (parameters) file_path: path to JSON file, 
                unit_residents: list of registered residents
    Return: Message of successful entry or message of error if there was an invalid entry.
    """
    try:

        # Opens and writes in the unit_residents file to add new entries
        with open(file_path, 'w') as file:
            json.dump(unit_residents, file, indent=4)    
        print(f"A new resident has been added to {file_path}.")
    
    # Manages error if user cannot add information
    except PermissionError:
        print(f"Error: Cannot write.")
   
    # Manage any other unexpected error
    except Exception as e:
        print("An expected error occurred", e)


def load_unit_body_corp(file_path):
    """
    Fetch information of body corporate payments from JSON file.
    (parameters) file_path: path to the JSON file that stores payments.
    Return: List of payments or empty list in case of error.
    """
    try:

        # Opens and reads JSON file of unit_body_corp
        with open(file_path, 'r') as file:
            unit_body_corp = json.load(file)
        return unit_body_corp
    
    # Manages error in case that file is missing
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist")
        return []
    
    # Manages any ohter unexpected error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def load_building_units(file_path):
    """
    Load a list with 20 possible unit numbers from JSON file.
    (parameters) file_path: path to the JSON file that stores unit numbers.
    Return: List of unit numbers or empty list in case of error.
    """
    try:

        # Opens and reads JSON file of building_units
        with open(file_path, 'r') as file:
            building_units = json.load(file)
        return building_units
    
    # Manages error in case that file is missing
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist")
        return []
   
    # Manages any ohter unexpected error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def load_floors(file_path):
    """
    Load a list with floor levels from JSON file.
    (parameters) file_path: path to the JSON file that stores floor levels.
    Return: List of floors or empty list in case of error.
    """
    try:

        # Opens and reads JSON file of building_units
        with open(file_path, 'r') as file:
            floors = json.load(file)
        return floors
    
    # Manages error in case that file is missing
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist")
        return []
    
    # Manages any ohter unexpected error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []