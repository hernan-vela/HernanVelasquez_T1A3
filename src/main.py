from add_delete_resid import add_new_resident, delete_unit_resident
from body_corporate import body_corp_unit_balance, global_balance
from total_counts import sum_residents_floor, total_residents_building
from units import display_residents, display_unit_info
from file_operations import load_unit_residents, save_residents, load_unit_body_corp, load_building_units, load_floors
from datetime import datetime
import os

# Define absolute path to root directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Use base_dir to define absolute path to JSON file
main_residents = os.path.join(base_dir, "data", "unit_residents.json")
bc_payments = os.path.join(base_dir, "data", "unit_body_corp.json")
unit_numbers = os.path.join(base_dir, "data", "building_units.json")
floor_levels = os.path.join(base_dir, "data", "floors.json")


# print(f"Main Residents Path: {main_residents}")
# print(f"BC Payments Path: {bc_payments}")
# print(f"Unit Numbers Path: {unit_numbers}")
# print(f"Floor Levels Path: {floor_levels}")


def main():
    """
    Upon calling numbers with their matching description, the user interacts with the Building Management Application
    from the Terminal. // Allows user to fetch information of residents, historical payments, add new residents, delete
    main residents information and save changes.
    """

    # Translate files loaded into variables used throughout the programme
    unit_residents = load_unit_residents(main_residents)
    unit_body_corp = load_unit_body_corp(bc_payments)
    building_units = load_building_units(unit_numbers)
    floors = load_floors(floor_levels)
    
    # Error handling if file is missing
    if not unit_residents:
        print("Not unit_residents loaded or an error occurred. Exiting.")
        return
    
    # Error handling if file is missing
    if not unit_body_corp:
        print("Not unit_body_corp loaded or an error occurred. Exiting.")
        return
    
    # Error handling if file is missing
    if not building_units:
        print("Not building_units loaded or an error occurred. Exiting.")
        return
    
    # Error handling if file is missing
    if not floors:
        print("Not floors loaded or an error occurred. Exiting.")
        return
    
    # # Print date and time at the top ot the Terminal
    print("\n", datetime.now().strftime("%y-%m-%d %H:%M:%S"))
   
    # Loop that shows app options
    while True:
        print("\nBuilding Management Application:")
        print("1. Display information about main residents")
        print("2. Display information per unit")
        print("3. Add new main resident")
        print("4. Delete main resident information")
        print("5. Calculate residents per floor level")   
        print("6. Total residents in the building")   
        print("7. Body Corporate balance per unit")   
        print("8. Global Body Corporate balance")
        print("9. Save changes and Exit")
        print("10. Exit (no save)\n")

        choice = input("Choose an option: ")
        
        # Match cases take user input and call its respective function
        if choice == '1':
            display_residents(unit_residents) 
        elif choice == '2':
            display_unit_info(unit_residents, building_units)
        elif choice == '3':
            add_new_resident(unit_residents, building_units)     
        elif choice == '4':
            delete_unit_resident(unit_residents) 
        elif choice == '5':
            sum_residents_floor(unit_residents) 
        elif choice == '6':
            total_residents_building(unit_residents) 
        elif choice == '7':
            body_corp_unit_balance(unit_body_corp, building_units) 
        elif choice == '8':
            global_balance(unit_body_corp)
        elif choice == '9':
            
            # Save changes made by user
            try:
                save_residents(main_residents, unit_residents)
                break
            except Exception as e:
                print(f"Error associating new info to a unit: {e}")
        elif choice == '10':
            print("-------------------")
            print("Exiting (unsaved).   Have a nice day!\n")
            return
        else:
            print("Not an option. Try again.")

if __name__ == "__main__":
    main()




