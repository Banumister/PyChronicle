from textual.screen import Screen
from textual.widgets import Static, Button
from textual.containers import Vertical

class DebuggerScreen(Screen):

    def compose(self):
        yield Vertical(
            Static("▶ Debugger Started", id="title"),

            Static("Program Running..."),
            Static("Waiting for Breakpoints..."),

            Button("⬅ Back", id="back")
        )

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "back":
            self.app.pop_screen()