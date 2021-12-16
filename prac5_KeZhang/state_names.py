"""
CP1404/CP5632 Practical
State names in a dictionary
KeZhang
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}


def main():
    print_formatted_states(CODE_TO_NAME)
    state_code = input("Enter short state: ").upper()
    while state_code != "":
        if state_code in CODE_TO_NAME:
            print(state_code, "is", CODE_TO_NAME[state_code])
        else:
            print("Invalid short state")
        print_formatted_states(CODE_TO_NAME)
        state_code = input("Enter short state: ").upper()


def print_formatted_states(code_to_name):
    """Print name and code of state in format."""
    for code, name in code_to_name.items():
        print(f'{code:3} is {name}')


if __name__ == '__main__':
    main()
