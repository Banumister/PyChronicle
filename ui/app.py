from textual.app import App
from dashboard import DashboardScreen   # or whatever you named the file


class PyChronicleApp(App):
    CSS_PATH = "styles.tcss"
    TITLE = "PyChronicle"
    SUB_TITLE = "AI Powered Time Travel Debugger"

    def on_mount(self) -> None:
        self.push_screen(DashboardScreen())


if __name__ == "__main__":
    PyChronicleApp().run()