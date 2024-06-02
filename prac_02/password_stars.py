"""
Prac_02 - Password Stars
"""


def main():
    """This program will get a password and print it out in asterisks"""
    password = get_password()
    print_in_asterisks(password)


def get_password():
    """Get a password from the user"""
    password = input("Enter your password: ")
    return password


def print_in_asterisks(prompt):
    """Print out input as asterisks"""
    prompt = '*' * len(prompt)
    print(prompt)


main()
