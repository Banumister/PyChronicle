from textual.screen import Screen
from textual.widgets import Static, Button
from textual.containers import Vertical

class SettingsScreen(Screen):

    def compose(self):
        yield Vertical(
            Static("⚙ Settings", id="title"),

            Static("Theme : Dark"),
            Static("Font Size : Medium"),
            Static("Auto Save : Enabled"),

            Button("⬅ Back", id="back")
        )

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "back":
            self.app.pop_screen()