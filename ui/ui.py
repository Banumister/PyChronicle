from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Static, Button


class PyChronicleUI(App):

    CSS = """
    Screen {
        align: center middle;
        background: #0d1117;
    }

    #title {
        content-align: center middle;
        color: cyan;
        text-style: bold;
        height: 3;
    }

    #menu {
        width: 50;
        height: auto;
        border: round cyan;
        padding: 1;
        content-align: center middle;
    }

    Button {
        width: 100%;
        margin: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        with Container(id="menu"):
            yield Static("🚀 PYCHRONICLE 🚀", id="title")
            yield Static("Time Travel Debugger\n")
            yield Button("▶ Start Debugging")
            yield Button("📜 Timeline")
            yield Button("📊 Variables")
            yield Button("📖 Execution History")
            yield Button("⚙ Settings")
            yield Button("❌ Exit")

        yield Footer()


if __name__ == "__main__":
   PyChronicleUI().run()
   from textual.widgets import Button

def on_button_pressed(self, event: Button.Pressed) -> None:
    button = event.button.label

    self.notify(f"You clicked: {button}")

    if "Start Debugging" in button:
        self.notify("Starting Debugger...")

    elif "Timeline" in button:
        self.notify("Opening Timeline...")

    elif "Variables" in button:
        self.notify("Opening Variables...")

    elif "Execution History" in button:
        self.notify("Opening History...")

    elif "Settings" in button:
        self.notify("Opening Settings...")

    elif "Exit" in button:
        self.exit()
    elif "settings" in button:
         self.notify("Opening Settings...")

    elif "Exit" in button:
        self.exit() 
   