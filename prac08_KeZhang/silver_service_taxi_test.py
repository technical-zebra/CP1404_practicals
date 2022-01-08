"""
CP1404/CP5632 Practical
SilverServiceTaxi test program
Ke Zhang
"""
from prac08_KeZhang.silver_service_taxi import SilverServiceTaxi


def main():
    silver_service_taxi = SilverServiceTaxi("Silver 1", 100, 5)
    silver_service_taxi.drive(40)
    print(silver_service_taxi)
    print(f"${silver_service_taxi.get_fare():.2f}")

    silver_service_taxi_2 = SilverServiceTaxi("Danger 2", 100, 10)
    silver_service_taxi_2.drive(90)
    print(silver_service_taxi_2)
    print(f"${silver_service_taxi_2.get_fare():.2f}")

    silver_service_taxi_3 = SilverServiceTaxi("Danger 3", 100, 2)
    silver_service_taxi_3.drive(18)
    print(silver_service_taxi_3)
    print(f"${silver_service_taxi_3.get_fare():.2f}")


if __name__ == '__main__':
    main()

