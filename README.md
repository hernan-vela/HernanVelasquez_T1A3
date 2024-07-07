# Coder Academy Full Stack Web Development Diploma
## HernanVelasquez_T1A3

#### Repository: [Github repo](https://github.com/hernan-vela/HernanVelasquez_T1A3)

# Building Management Application (Terminal App)

## Code Styling - PEP8

The code styling used for this project is PEP8, following its guidelines as explained in Python website (2023)[^1].

## 



## Application layout

The Building Management Application, run from the Terminal, is thought to handle the information of a building with five-floor levels (G, 1, 2, 3, 4) and four units per level. It stores information about the full name of the main resident of the unit, the status of owner / lessee, the number of residents living in such unit, and the balance of Body Corporate per unit and globally.

The application uses three files with JSON extension, designed, named and stored as global resources for all the functions throughout the Building Management App. The *'unit_resident.json'* with information of owners / lessees occupying each unit, is organised as an array of dictionaries in a list. The *'body_corporate_balance.json'* , contains historical payments of the body corporate as an array of dictionaries in a list. Last, a *'building_units.json'* file, which is a list of all possible unit numbers in the building.

The application is built such as the only changeable file is the *'unit_residents.json'*, from which is possible to delete entries of residents who may have left the building, or add new residents who bought or rented a unit.

The modules of the *main function* (main.py) are coded in external Python files, and grouped according to their use, in packages later imported to the 'main.py' function.

The 'main.py' function is designed as a match case, which allows the user to select tasks to perform with the keyboard. Then, the user follows the instructions until the requests in form of inputs, return a satisfactory output, or a way to terminate the process before finishing its task.

## Main Features

The features showed from the user interface are:

1. **Display info about main residents**

Iterates through a JSON file called 'unit_residents' that stores unit number, first name, last name, owner / tenant status and number of residents living in there. The loop captures every entry per unit and displays them in an organised list.

2. **Display information per unit**

This function requests input from the user, necessary to match at least any of the 20 units in the building that are comprised in 'building_units.json'. First, the input enters a validity loop, and the value is converted to uppercase, to cover units in the G Level.
In case of an invalid value, the user is prompted to try again, press 'q' or 'Q' to exit the validity loop and return to the main menu.

Using a definite loop the programme confirms if the key exists in the database of 'unit_residents' and if so, it will print a descending list of the respective entry for the unit (input), resident full name, owner/tenant status and number of people living in this unit. Otherwise, the system will print a message asserting the unit's existence in the building, but not information recorded for this unit.

3. **Add new main resident**

The app requests input from the user to populate a new entry that could be stored in the 'unit_residents' file, if there is not entry for that unit number, and the user decides to save it. The keys requested are:

```
{
  'unit':
  'first name':
  'last name':
  'status':
  'num_residents':
}

```
The program unfolds as follow:

3.1 *Unit* : the user's input enters a validity loop until is true or the user escapes it and it is returned to the main menu. First, the input is converted to upper case to cover unit numbers in G level.

A conditional can take the user out of the loop when pressing 'q' or 'Q'. Simultaneously the possible values are assessed, and errors nicely handled with other conditionals.

If the input is a valid unit number but already occupied, the user cannot overwrite the entry and the user is taken out the programme to the main menu; else if the input is an invalid character, the user can try again or exit the programme by pressing 'q / Q'. Finally, the validity loop restarts until is satisfied with a valid unit number, or the user escapes the programme.

3.2 *First name* and *last name*: These two behave similarly. The user is asked to type a name, and the program checks that is an alphabetic entry, if is a non-alphabetical input, the user is prompted to try again or press 'q / Q' to exit the program. If the entry is valid, the program moves forward.

3.4 *Status* : The condition of owner or tenant is asked, and the user is advised to answer 'yes' for owner, and 'no' for tenant. A loop validates the answers taking any combination of upper or lowercase of yes/no as valid. Again, an invalid input asks the question or invites the user to press 'q / Q' to exit the program. If the input is valid the program moves forward

3.5 *Number of residents* : Final key of the block. The input goes through a validity loop, with 'num_residents' valid if it is an integer > 0. A conditional offers the user to type 'q / Q' to return to the main menu, else if the input < 0, the user is prompted to enter an integer > 0; else if the input = 0, a message says that at least one resident should live in. Finally, if there is another type of error, the user is offered to press 'q / Q' to escape the loop or try again an the validity loop restarts.

4. **Delete main resident information**

Uses 'unit_resident.json' file to iterate through it. This file contains


The user's input goes into a validity loop. The user is asked to enter a unit number that they want to vacate or press 'q / Q' to quit. If they press 'q / Q' the program ends and goes back to the main menu.

As character validation, the program checks if is valid alphanumeric unit number. Invalid characters will return a message and the loop asks the user for an input again.

If the entry is valid, a loop iterates through the database of 'unit-residents'. If there is a key 'unit' that matches the input, the entry is vacated as if the unit were vacated. End of the loop.

5. **Calculate residents per floor level**

It starts with a validity loop that makes the code keeps asking the user for input until they decide to terminate by pressing 'q / Q'.

The user is asked for an input in form of a level (G, 1, 2, 3, 4) or press 'q' to quit. The input is converted to uppercase to match the ground level. If the user enters 'q / Q', the loops breaks, program ended.

To manage invalid level inputs, there is a local variable called *'floors'* such as a list that includes all the possible values for building levels. An error is printed if the input is not in *'floors'*

The count of residents in the building is initialized as 'floor_residents' is zero, then the code iterates through 'unit_residents' and for all unit numbers, such as the first character of the pair value matches the valid user's input, the number of residents in that unit is added to 'floor_residents'.

After iterating across all the units in the requested floor, the total is printed and displayed in the Terminal.

6. **Total residents in the building**

This function simply iterates through 'unit_residents', after initializing the count as 'total_residents' equals zero, the code goes in a loop that iterates each 'unit' in 'unit_residents' and adds the number of residents to the 'total_residents'. Once all the list has been checked, the final value is printed as number of total residentes registered in the building.

7. **Body Corporate balance per unit**

This function starts with a validity loop and will constantly prompt the user for input until they choose to escape by pressing 'q', then the loop breaks.
The function checks if the user's input is in 'building_units' list. If not, it prints a nice error message and prompts the user again.

The function initializes the variable 'balance' to 'None', then iterates over 'unit_body_corp' list to find the "Unit" that matches with the user's input, it finds the "Body Corporate balance" and assigns the value to the 'balance', and breaks the loop.

If the 'balance' is different from 'None', it prints current date and time, unit number and balance.

When no balance is found, it shows a message indicating that there is not balance information for such unit.

8. **Global Body Corporate Balance**

A variable is initialized as 'total_bc_balance' equals zero. Then, the function iterates over each entry in the 'unit_body_corp' list, for each entry it takes the "Body Corporate balance" and adds it to the 'total_bc_balance'.

After iterating over all the list entries, it prints the total Body Corporate balance.

9. **Save changes and exit**

This function take a path to the JSON file where the data will be stored and the 'unit_residents' list that needs to be saved.

The function opens the file in write mode , writes the information that the user might have modified through the features of adding/deleting residents, and prints a confirmation of information saved.

There are two Exception errors, one in case that the user does not have rights to changed information and another for any unexpected error.

10. **Exit (no save)**

By choosing this option the program prints a message indicating that the app will close without saving changes, and it finalises the terminal app.


:




## References 

[^1]: Python Enhancements Proposals by Python (2023), PEP8 - Style Guide for Python Code, accessed 01 July 2024, https://peps.python.org/pep-0008/

