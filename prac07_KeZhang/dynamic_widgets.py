"""
CP1404/CP5632, IT@JCU
Dynamic Kivy Widgets demo program
Ke Zhang
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    output_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.animal_to_sound = {"Cat": "meow", "Cattle": "moo", "Chicken": "cluck", "Dog": "awoo"}
        self.output_text = "Select an animal"

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for animal in self.animal_to_sound:
            animal_button = Button(text=animal)
            animal_button.bind(on_release=self.press_entry)
            self.root.ids.animals_layout.add_widget(animal_button)

    def press_entry(self, instance):
        """handle buttons when pressed and output sound text"""
        name = instance.text
        self.output_text = f"{self.animal_to_sound[name]}"


DynamicWidgetsApp().run()
