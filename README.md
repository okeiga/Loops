# Python Programs for CS50 - Loops

This repository contains a collection of Python programs created for the CS50 course, specifically focusing on loops and user input. Each program demonstrates different functionalities and adheres to specific requirements.

## Programs

### 1. `camel.py`
Prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.

### 2. `coke.py`
Prompts the user to insert a coin, one at a time, and informs the user of the amount due each time. Once the user has inputted at least 50 cents, it outputs how many cents in change the user is owed.

### 3. `twttr.py`
Prompts the user for a string of text and outputs that same text but with all vowels (A, E, I, O, and U) omitted, regardless of whether they are in uppercase or lowercase.

### 4. `plates.py`
Implements a program that prompts the user for a vanity plate and checks if it meets the following requirements:
- All vanity plates must start with at least two letters.
- Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
- Numbers cannot be used in the middle of a plate; they must come at the end. For example, `AAA222` would be acceptable, while `AAA22A` would not.
- The first number used cannot be a ‘0’.
- No periods, spaces, or punctuation marks are allowed.

The program outputs "Valid" if the vanity plate meets all requirements or "Invalid" if it does not.

### 5. `nutrition.py`
The program prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits.

## Usage

To run any of these programs, ensure you have Python installed on your machine. Open a terminal, navigate to the directory where the program is located, and execute the program using the command:

```bash
python filename.py

