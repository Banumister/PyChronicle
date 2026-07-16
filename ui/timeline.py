from textual.screen import Screen
from textual.widgets import Static, Button
from textual.containers import Vertical,Center


class TimelineScreen(Screen):

    def compose(self):
        yield Vertical(
            Static("📜 EXECUTION TIMELINE", id="title"),
            Static("━━━━━━━━━━━━━━━━━━━━━━━━━━━━", id="line"),

            Static("🟢 Program Started"),
            Static("│"),

            Static("📂 Loaded sample.py"),
            Static("│"),

            Static("⚙ Entered main()"),
            Static("│"),

            Static("▶ Executing Line : 25"),
            Static("│"),

            Static("📌 Variable x = 10"),
            Static("│"),

            Static("✅ Execution Completed"),
            Static(""),
            Center(
                Button("🏠 Return Home", id="back"),
            ),

            Static("")
        )

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "back":
            self.app.pop_screen()