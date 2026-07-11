from textual.screen import Screen
from textual.widgets import Static, Button
from textual.containers import Vertical


class TimelineScreen(Screen):

    def compose(self):
        yield Vertical(
            Static("📜 Timeline", id="title"),

            Static("Current Event : 1"),
            Static("Current Line : 25"),
            Static("Function : main()"),

            Button("⬅ Back", id="back")
        )
    def on_button_pressed(self, event: Button.Pressed):

        if event.button.id == "back":
            self.app.pop_screen() 