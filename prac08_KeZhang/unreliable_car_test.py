"""
CP1404/CP5632 Practical
UnreliableCar test program
Ke Zhang
"""
from prac08_KeZhang.unreliable_car import UnreliableCar


def main():
    unreliable_car = UnreliableCar("Danger 1", 100, 50)
    unreliable_car.drive(40)
    print(unreliable_car)

    unreliable_car_2 = UnreliableCar("Danger 2", 100, 10)
    unreliable_car_2.drive(50)
    print(unreliable_car_2)

    unreliable_car_3 = UnreliableCar("Danger 3", 100, 90)
    unreliable_car_3.drive(60)
    print(unreliable_car_3)


if __name__ == '__main__':
    main()
