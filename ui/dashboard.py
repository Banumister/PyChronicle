from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Static, Button
from textual.screen import Screen

# Import other screens
from timeline import TimelineScreen
from variables import VariablesScreen
from history import HistoryScreen
from settings import SettingsScreen


class DashboardScreen(Screen):

    def compose(self) -> ComposeResult:
        with Vertical(id="menu"):
            yield Static(" ✦  PYCHRONICLE  ✦", id="title")
            yield Static("AI Powered Time Travel Debugger", id="subtitle")
            yield Static("────────────────────────────", id="line")

            yield Button(" Start Debugging", id="start")
            yield Button("  Timeline", id="timeline")
            yield Button("  Variables", id="variables")
            yield Button("  Execution History", id="history")
            yield Button("   Settings", id="settings")
            yield Button("  Exit", id="exit-btn")

            yield Static("v1.0  •  Developed by Team PyChronicle", id="footer")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id

        if button_id == "start":
            self.notify("Starting Debugger...", severity="information")
            # Later you can push DebuggerScreen here

        elif button_id == "timeline":
            self.app.push_screen(TimelineScreen())

        elif button_id == "variables":
            self.app.push_screen(VariablesScreen())

        elif button_id == "history":
            self.app.push_screen(HistoryScreen())

        elif button_id == "settings":
            self.app.push_screen(SettingsScreen())

        elif button_id == "exit-btn":
            self.app.exit()