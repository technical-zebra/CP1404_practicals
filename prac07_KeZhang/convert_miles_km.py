"""
CP1404/CP5632 Practical
Kivy GUI program to convert mile to km
Ke Zhang
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM_MULTIPLIER = 1.60934


class ConvertMilesToKmsApp(App):
    """ ConvertMilesToKmsApp is a Kivy App for convert mile to km """
    output_km = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_km = "Type distance in miles"
        return self.root

    def calculate_km(self, text):
        """ handle calculation (could be button press or other call), output result to label widget """
        miles = self.convert_to_number(text)
        result = round(miles * MILES_TO_KM_MULTIPLIER, 3)
        self.output_km = str(result)

    def handle_increment(self, text, value):
        """Handle up/down button press, update the text input with new value, call calculation function."""
        miles = self.convert_to_number(text) + value
        self.root.ids.input_label.text = str(miles)

    @staticmethod
    def convert_to_number(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesToKmsApp().run()
