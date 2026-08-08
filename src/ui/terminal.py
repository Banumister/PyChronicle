from src.storage.database import TraceDatabase
from src.storage.time_travel import TimeTravelEngine


class TerminalUI:
    """
    Terminal interface for navigating recorded
    PyChronicle execution events.
    """

    def __init__(self, database_name="pychronicle.db"):
        self.database = TraceDatabase(database_name)
        self.events = self.database.fetch_event_objects()
        self.engine = TimeTravelEngine(self.events)

    def display_event(self, event):
        print()
        print("=" * 50)

        if event is None:
            print("No execution event available.")
            return

        print("CURRENT EVENT")
        print("=" * 50)
        print(f"Event ID   : {event['id']}")
        print(f"Event      : {event['event']}")
        print(f"Function   : {event['function']}")
        print(f"Line       : {event['line']}")
        print(f"Variable   : {event['variable']}")
        print(f"Value      : {event['value']}")
        print(f"Timestamp  : {event['timestamp']}")

    def display_state(self):
        state = self.engine.state()

        print()
        print("=" * 50)
        print("PROGRAM STATE")
        print("=" * 50)

        if not state:
            print("No variables recorded.")
            return

        for variable, value in state.items():
            print(f"{variable} = {value}")

    def display_help(self):
        print()
        print("=" * 50)
        print("PYCHRONICLE COMMANDS")
        print("=" * 50)
        print("n  - Next event")
        print("p  - Previous event")
        print("j  - Jump to event")
        print("s  - Show current state")
        print("c  - Show current event")
        print("q  - Quit")

    def run(self):
        if not self.events:
            print("No execution events found.")
            self.database.close()
            return

        print()
        print("=" * 50)
        print("PYCHRONICLE")
        print("TIME-TRAVEL DEBUGGER")
        print("=" * 50)

        self.display_event(self.engine.current())
        self.display_state()
        self.display_help()

        while True:
            command = input("\nCommand: ").strip().lower()

            if command == "n":
                self.display_event(self.engine.next())
                self.display_state()

            elif command == "p":
                self.display_event(self.engine.previous())
                self.display_state()

            elif command == "j":
                event_id = input("Enter event ID: ").strip()

                try:
                    event_id = int(event_id)
                except ValueError:
                    print("Event ID must be an integer.")
                    continue

                event = self.engine.jump(event_id)

                if event is None:
                    print(f"Event {event_id} not found.")
                else:
                    self.display_event(event)
                    self.display_state()

            elif command == "s":
                self.display_state()

            elif command == "c":
                self.display_event(self.engine.current())

            elif command == "q":
                break

            else:
                print("Unknown command.")
                self.display_help()

        self.database.close()