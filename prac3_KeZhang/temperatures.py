"""
CP1404 Practices
Ke Zhang
temperatures: a program that convert temperature from Celsius to Fahrenheit or vice versa.
"""


def main():
    """Program start."""
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print("Result: {:.2f} F".format(convert_to_fahrenheit(celsius)))

        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print("Result: {:.2f} C".format(convert_to_celsius(fahrenheit)))

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_fahrenheit(celsius):
    """Input celsius then convert celsius to fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_to_celsius(fahrenheit):
    """Input fahrenheit then convert fahrenheit to celsius."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


if __name__ == '__main__':
    main()
