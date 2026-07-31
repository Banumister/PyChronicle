from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Static, Button
from textual.screen import Screen


class VariablesScreen(Screen):

    def compose(self) -> ComposeResult:
        with Vertical(classes="screen-panel"):
            yield Static("📊  VARIABLES", classes="screen-title")
            yield Static("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            
            yield Static("")
            yield Static("  x            =  42", classes="screen-content")
            yield Static("  name         =  'Dharani'", classes="screen-content")
            yield Static("  is_active    =  True", classes="screen-content")
            yield Static("  counter      =  7", classes="screen-content")
            yield Static("  data         =  [10, 20, 30]", classes="screen-content")
            yield Static("  result       =  None", classes="screen-content")
            yield Static("  temperature  =  36.6", classes="screen-content")
            yield Static("")
            
            yield Button("←  Back to Menu", id="back")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.app.pop_screen()