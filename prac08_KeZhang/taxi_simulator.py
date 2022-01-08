"""
CP1404/CP5632 Practical
Taxi simulator program
Ke Zhang
"""
from prac08_KeZhang.car import Car
from prac08_KeZhang.silver_service_taxi import SilverServiceTaxi
from prac08_KeZhang.taxi import Taxi

MENU = "Let's drive!\nq)uit, c)hoose taxi, d)rive\n>>> "


def main():
    """Write a taxi simulator program that uses your Taxi and SilverServiceTaxi
       classes. Each time, until they quit:
       The user should be presented with a list of available taxis and get to
       choose one. Then they should say how far they want to drive.
       At the end of each trip, show them the price and add it to their bill.
       """
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available: ")
            display_taxis(taxis)
            current_taxi = int(input("Choose taxi: "))
            if current_taxi in range(len(taxis)):
                print(f"Bill to date: ${bill_to_date:.2f}")
            else:
                print(f"Invalid taxi choice\nBill to date: ${bill_to_date:.2f}")
        elif choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                taxis[current_taxi].start_fare()
                taxis[current_taxi].drive(int(input("Drive how far? ")))
                trip_cost = taxis[current_taxi].get_fare()
                bill_to_date += trip_cost
                print(f"Your {taxis[current_taxi].name} trip cost you ${trip_cost:.2f}")
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        choice = input(MENU).upper()
    print(f"Total trip cost: ${bill_to_date}\nTaxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")


if __name__ == '__main__':
    main()

