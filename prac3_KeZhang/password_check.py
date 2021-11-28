"""
CP1404
Ke Zhang
"""


def main():
    password = get_password()


def get_password():
    password = input('Enter your password: ')
    minimum_length = 5
    while len(password) != minimum_length:
        print('Invalid length! Try again!')
        password = input('Enter your password: ')
    print(len(password) * '*')
    return password


if __name__ == '__main__':
    main()
