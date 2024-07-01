import json

def load_unit_residents(file_path):
    """
    Fetch information of residents from JSON file.
    (parameters) file_path: path to the JSON file.
    Return: List of residents or empty list in case of error.
    """
    try:
        with open(file_path, 'r') as file:
            residents = json.load(file)
        return residents
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
    
def save_residents(file_path, residents):
    """
    Save information of residents in a JSON file.
    (parameters) file_path: path to JSON file, residents: list of residents
    Return: Error message in case of invalid entry.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(residents, file, indent=4)
        print(f"A new resident has been added to {file_path}.")
    except PermissionError:
        print(f"Error: You need rights to add information of new residents.")
    except Exception as e:
        print("An expected error occurred", e)