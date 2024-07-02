from file_operations import load_unit_residents, save_residents
from unit_operations import display_residents, add_new_resident

residents_file = '../data/unit_residents.json'
body_corp_file = '../data/unit_body_corp.json'

def main():

    residents = load_unit_residents(residents_file)

if not residents:
    print("Building empty (oh, oh!) or an error occurred. Exiting.")
    return
while True:
    print("\nBuilding Management:")
    print()