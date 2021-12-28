"""CP1404/CP5632 Practical - Car class """



class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine whether a ProgrammingLanguage is dynamic or not."""
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        """Display information about this ProgrammingLanguage object."""
        return f'{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}'
