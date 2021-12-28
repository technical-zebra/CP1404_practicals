"""CP1404/CP5632 Practical - Guitar class."""
import datetime

class Guitar:
    """Represent a Car object."""

    def __init__(self, name, year, cost):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = int(year)
        self.cost = float(cost)
        print(f"{self.name} ({self.year}) : ${self.cost:.2f} added.")

    def __str__(self):
        """Display information about this Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}."

    def get_age(self):
        """Calculate the age of this guitar."""
        age = int(datetime.datetime.now().year) - self.year
        return age

    def is_vintage(self):
        """Determine whether a Guitar is vintage or not."""
        age = self.get_age()
        response = True if age >= 18 else False
        return response
