from textual.screen import Screen
from textual.widgets import Static, Button
from textual.containers import Vertical

class VariablesScreen(Screen):

    def compose(self):
        yield Vertical(
            Static("📊 Variables"),

            Static("x = 10"),
            Static("y = 20"),
            Static("result = 30"),

            Button("⬅ Back", id="back")
        )

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "back":
            self.app.pop_screen()