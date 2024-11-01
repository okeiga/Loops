def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    # Check if all conditions are met
    return starts_with_two_letters(plate) and length_valid(plate) and numbers_at_end(plate) and no_punctuation(plate)

def starts_with_two_letters(plate):
    # Check if the first two characters are alphabetic
    return plate[:2].isalpha()

def length_valid(plate):
    # Check if the plate length is between 2 and 6 characters
    return 2 <= len(plate) <= 6

def numbers_at_end(plate):
    # Check for the correct use of numbers:
    # - Numbers can only appear at the end of the plate
    # - The first number cannot be '0' if numbers are used
    for i in range(len(plate)):
        if plate[i].isdigit():
            # Check if all characters after the first number are also digits
            if not plate[i:].isdigit():
                return False
            # Ensure the first number is not '0'
            if plate[i] == '0':
                return False
            break
    return True

def no_punctuation(plate):
    # Ensure no punctuation marks or spaces in the plate
    return all(char.isalnum() for char in plate)

main()
