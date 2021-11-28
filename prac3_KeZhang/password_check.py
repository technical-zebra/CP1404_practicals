"""
CP1404 Practices
Ke Zhang
password_check: a program that asks the user for a password and prints asterisks based on its length.
"""


def main():
    """Program start."""
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """Input password then print asterisks based on length of password."""
    print(len(password) * '*')


def get_password():
    """Get password from user input then return this password."""
    password = input('Enter your password: ')
    minimum_length = 5
    while len(password) != minimum_length:
        print('Invalid length! Try again!')
        password = input('Enter your password: ')
    return password


if __name__ == '__main__':
    main()
