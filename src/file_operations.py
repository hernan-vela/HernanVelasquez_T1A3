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
    Return: Message of successful entry or message of error if there was an invalid entry.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(residents, file, indent=4)
        print(f"A new resident has been added to {file_path}.")
    except PermissionError:
        print(f"Error: You need rights to add information of new residents.")
    except Exception as e:
        print("An expected error occurred", e)


def load_unit_body_corp(file_path):  # REFERENCE A FILE OF BODY CORPORATE????
    """
    Fetch information of body corporate payments from JSON file.
    (parameters) file_path: path to the JSON file that stores payments.
    Return: List of payments or empty list in case of error.
    """
    try:
        with open(file_path, 'r') as file:
            body_coporate = json.load(file)
        return body_corporate
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def save_unit_body_corp(file_path, body_corporate):
    """
    Save information of body corporate payments in a JSON file.
    (parameters) file_path: path to JSON file with historic payments, body_corporate: list of body corporate payments
    Return: Message of successful addition or message of error in case of invalid entry.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(body_corporate, file, indent=4)
        print(f"A new balance has been added to {file_path}.")
    except PermissionError:
        print(f"Error: You need rights to add information about residents.")
    except Exception as e:
        print("An expected error occurred", e)
