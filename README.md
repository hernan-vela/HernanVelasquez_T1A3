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
The programme unfolds as follow:

3.1 *Unit* : the user input enters a validty loop until is true or the user escapes it and it is returned to the main menu. First, the input is converted to upper case to cover unit numbers in G level. 
To avoid over




3.2 *First name* : 

3.3 *Last Name* :

3.4 *Status* :

3.5 *Number of residents* :








Develop a list of features that will be included in the application. It must include:

- at least THREE features

- describe each feature, providing a walkthrough of the logic of the application.


Note: Ensure that your features above allow you to demonstrate your understanding of the following language elements and concepts:

- use of variables and the concept of variable scope

- loops and conditional control structures

- error handling




## References 

[^1]: Python Enhancements Proposals by Python (2023), PEP8 - Style Guide for Python Code, accessed 01 July 2024, https://peps.python.org/pep-0008/

