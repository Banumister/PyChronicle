from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Static, Button
from textual.screen import Screen


class HistoryScreen(Screen):

    def compose(self) -> ComposeResult:
        with Vertical(classes="screen-panel"):
            yield Static("📖  EXECUTION HISTORY", classes="screen-title")
            yield Static("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            
            yield Static("")
            yield Static("  01.  Debugging session started", classes="screen-content")
            yield Static("  02.  Entered main function", classes="screen-content")
            yield Static("  03.  Called process_data()", classes="screen-content")
            yield Static("  04.  Variable 'x' changed → 42", classes="screen-content")
            yield Static("  05.  Condition checked (True)", classes="screen-content")
            yield Static("  06.  Exception raised at line 47", classes="screen-content")
            yield Static("  07.  Session paused by user", classes="screen-content")
            yield Static("")
            
            yield Button("←  Back to Menu", id="back")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.app.pop_screen()