# Coder Academy Full Stack Web Development Diploma
## HernanVelasquez_T1A3

#### Repository: [Github repo](https://github.com/hernan-vela/HernanVelasquez_T1A3)

# Building Management Application (Terminal App)

## Code Styling - PEP8

The code styling used for this project is PEP8, following its guidelines as explained in Python website (2023)[^1].

## 



## Main Features

The Building Management Application, run from the Terminal, is thought to handle the information of a building with five-floor levels (G, 1, 2, 3, 4) and four units per level. It stores information about the full name of the main resident of the unit, the status of owner / lessee, the number of residents living in such unit, and the balance of Body Corporate per unit and globally.

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

The user's input goes into a validity loop. The user is asked to enter a unit number that they want to vacate or press 'q / Q' to quit. If they press 'q / Q' the program ends and goes back to the main menu.

As character validation, the program checks if is valid alphanumeric unit number. Invalid characters will return a message and the loop asks the user for an input again.

If the entry is valid, a loop iterates through the database of 'unit-residents'. If there is a key 'unit' that matches the input, the entry is vacated as if the unit were vacated. End of the loop.

5. **Calculate residents per floor level**





Develop a list of features that will be included in the application. It must include:

- at least THREE features

- describe each feature, providing a walkthrough of the logic of the application.


Note: Ensure that your features above allow you to demonstrate your understanding of the following language elements and concepts:

- use of variables and the concept of variable scope

- loops and conditional control structures

- error handling




## References 

[^1]: Python Enhancements Proposals by Python (2023), PEP8 - Style Guide for Python Code, accessed 01 July 2024, https://peps.python.org/pep-0008/

