from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Static, Button
from textual.screen import Screen


class SettingsScreen(Screen):

    def compose(self) -> ComposeResult:
        with Vertical(classes="screen-panel"):
            yield Static("⚙  SETTINGS", classes="screen-title")
            yield Static("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            
            yield Static("")
            yield Static("  Theme              :  Dark Cyan", classes="screen-content")
            yield Static("  Auto Save          :  Enabled", classes="screen-content")
            yield Static("  Debug Level        :  Detailed", classes="screen-content")
            yield Static("  AI Suggestions     :  On", classes="screen-content")
            yield Static("  Max History Steps  :  500", classes="screen-content")
            yield Static("  Sound Effects      :  Off", classes="screen-content")
            yield Static("  Time Travel Mode   :  Enabled", classes="screen-content")
            yield Static("")
            
            yield Button("←  Back to Menu", id="back")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.app.pop_screen()