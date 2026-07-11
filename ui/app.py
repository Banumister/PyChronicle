from textual.app import App
from dashboard import DashboardScreen


class PyChronicleApp(App):

    CSS_PATH = "styles.tcss"

    def on_mount(self):
        self.push_screen(DashboardScreen())


if __name__ == "__main__":
    PyChronicleApp().run()