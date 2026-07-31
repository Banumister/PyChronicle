from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Static, Button
from textual.screen import Screen


class TimelineScreen(Screen):

    def compose(self) -> ComposeResult:
        with Vertical(classes="screen-panel"):
            yield Static("📜  TIMELINE", classes="screen-title")
            yield Static("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            
            yield Static("")
            yield Static("  ①  Step 01  →  Program Started", classes="screen-content")
            yield Static("  ②  Step 02  →  main() entered", classes="screen-content")
            yield Static("  ③  Step 03  →  Variable initialized", classes="screen-content")
            yield Static("  ④  Step 04  →  Condition evaluated", classes="screen-content")
            yield Static("  ⑤  Step 05  →  Function called", classes="screen-content")
            yield Static("  ⑥  Step 06  →  Loop iteration #3", classes="screen-content")
            yield Static("  ⑦  Step 07  →  Return value received", classes="screen-content")
            yield Static("")
            
            yield Button("←  Back to Menu", id="back")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.app.pop_screen()