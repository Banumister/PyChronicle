from database import save_history 
from debugger import DebuggerScreen 
from history import HistoryScreen 
from settings import SettingsScreen 
from variables import VariablesScreen 
from variables import VariablesScreen 
from timeline import TimelineScreen 
from textual.screen import Screen
from textual.containers import Vertical
from textual.widgets import Static, Button


class DashboardScreen(Screen):

    def compose(self):
     yield Vertical(
        Static("🚀 PYCHRONICLE 🚀", id="title"),
        Static("AI powered Time Travel Debugger",id="subtitle"),
        Button("▶ Start Debugging", id="debug"),
        Button("📜 Timeline", id="timeline"),
        Button(" Variables", id="variables"),
        Button("📖 History", id="history"),
        Button("⚙ Settings", id="settings"),
        Button("❌ Exit", id="exit"),
        Static("version 1.0| Developed by Team PyChronicle", id="footer"),
    )
    def on_button_pressed(self, event: Button.Pressed):
     if event.button.id == "debug":
        save_history("sample.py","Started Debugging")
        self.app.push_screen(DebuggerScreen())

     elif event.button.id == "timeline":
        self.app.push_screen(TimelineScreen())

     elif event.button.id == "variables":
        self.app.push_screen(VariablesScreen())

     elif event.button.id == "history":
        self.app.push_screen(HistoryScreen())

     elif event.button.id == "settings":
        self.app.push_screen(SettingsScreen())

     elif event.button.id == "exit":
        self.app.exit()
