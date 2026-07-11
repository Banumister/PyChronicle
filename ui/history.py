from textual.screen import Screen
from textual.widgets import Static, Button
from textual.containers import Vertical
from database import get_history

class HistoryScreen(Screen):

    def compose(self):
        history = get_history()

        items = [Static("📄 History")]

        for row in history:
            items.append(
                Static(f"ID: {row[0]} | File: {row[1]} | Event: {row[2]}")
            )

        items.append(Button("← Back", id="back"))

        yield Vertical(*items)

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "back":
            self.app.pop_screen()