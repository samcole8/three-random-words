"""Common functions used by multiple parts of the program."""


import math


def integer_test(message, lower_limit=-math.inf, upper_limit=math.inf):
    """Take input and repeat until valid integer is provided."""
    valid = False
    while not valid:
        try:
            # Check datatype.
            integer_value = int(input(f"{message}:  "))
            # Check limits.
            if lower_limit <= integer_value <= upper_limit:
                valid = True
            else:
                error(f"Value out of bounds ({lower_limit} - {upper_limit})")
        except ValueError:
            error("Value is not a whole number.")
    return integer_value


def return_prompt():
    """Display simple return prompt."""
    input("Press ENTER to return to the menu.")


def error(message):
    """Display simple error message."""
    print(f"ERROR: {message}")
