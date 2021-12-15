"""
CP1404/CP5632 Practical
Hex colour codes in a dictionary
KeZhang
"""
NAME_TO_COLOUR_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                       "alizarin crimson": "#e32636",
                       "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc", "antiquewhite": "#faebd7",
                       "apricot": "#fbceb1", "Aqua": "#00ffff"}


def main():
    print_formatted_colour_codes(NAME_TO_COLOUR_CODE)
    colour_name = input("Enter colour name: ").lower()
    while colour_name != "":
        if colour_name in NAME_TO_COLOUR_CODE:
            print(colour_name, "is", NAME_TO_COLOUR_CODE[colour_name])
        else:
            print("Invalid colour name!")
        print_formatted_colour_codes(NAME_TO_COLOUR_CODE)
        colour_name = input("Enter colour name: ").lower()


def print_formatted_colour_codes(code_to_name):
    for name, code in code_to_name.items():
        print(f'{name} is {code}')


if __name__ == '__main__':
    main()
