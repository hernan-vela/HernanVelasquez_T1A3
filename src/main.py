from file_operations import load_unit_residents, save_residents, load_unit_body_corp, load_building_units, load_floors
from unit_operations import display_residents, display_unit_info, add_new_resident, delete_unit_resident, sum_residents_floor, total_residents_building
from body_corp_operations import bodyCorp_unit_balance, global_balance
from datetime import datetime
import json

main_residents = '../data/unit_residents.json'
bc_payments = '../data/unit_body_corp.json'
unit_numbers = '../data/building_units.json'
floor_levels = '../data/floors.json'

def main():
    """
    Main functions that compiles packages and modules to display 
    ...
    ...
    """
    unit_residents = load_unit_residents(main_residents)
    unit_body_corp = load_unit_body_corp(bc_payments)
    building_units = load_building_units(unit_numbers)
    floors = load_floors(floor_levels)
    
    if not unit_residents:
        print("Not unit_residents loaded or an error occurred. Exiting.")
        return
    
    if not unit_body_corp:
        print("Not unit_body_corp loaded or an error occurred. Exiting.")
        return
    
    if not building_units:
        print("Not building_units loaded or an error occurred. Exiting.")
        return
    
    if not floors:
        print("Not floors loaded or an error occurred. Exiting.")
        return
    
    while True:
        print("\nBuilding Management Application:")
        print("1. Display info about main residents")
        print("2. Display info per unit")
        print("3. Add new main resident")
        print("4. Delete main resident info")
        print("5. Calculate registered residents per floor level")   
        print("6. Total registered residents in the building")   
        print("7. Body Corporate balance per unit")   
        print("8. Global Body Corporate balance")
        print("9. Save changes and Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            display_residents(unit_residents) # REVIEW ARGUMENT
        elif choice == '2':
            display_unit_info(unit_residents) # REVIEW ARGUMENT
        elif choice == '3':
            add_new_resident(unit_residents) # REVIEW ARGUMENT    
        elif choice == '4':
            delete_unit_resident(unit_residents) # REVIEW ARGUMENT
        elif choice == '5':
            sum_residents_floor(unit_residents) # REVIEW ARGUMENT
        elif choice == '6':
            total_residents_building(unit_residents) # REVIEW ARGUMENT
        elif choice == '7':
            bodyCorp_unit_balance(unit_body_corp) # REVIEW ARGUMENT
        elif choice == '8':
            global_balance(unit_body_corp)
        elif choice == '9':
            try:
                save_residents(main_residents, unit_residents)
                break
            except Exception as e:
                print(f"Error associating new info to a unit: {e}")
        else:
            print("Not an option. Try again.")

if __name__ == "__main__":
    main()




