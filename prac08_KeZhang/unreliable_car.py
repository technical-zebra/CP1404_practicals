"""
CP1404/CP5632 Practical
UnreliableCar class
Ke Zhang
"""
from prac08_KeZhang.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        if 100 >= reliability >= 0:
            self.reliability = float(reliability)
        else:
            print("Initialization failed")
            self.reliability = 0

    def __str__(self):
        """Return a string like a Car but based on reliability."""
        return f"{super().__str__()}, reliability: {self.reliability}"

    def drive(self, distance):
        """Drive like parent Car if random number less than reliability."""
        temp_num = random.randint(0, 100)
        if temp_num >= self.reliability:
            distance = 0
            print("Drive failed")
        distance_driven = super().drive(distance)
        return distance_driven
