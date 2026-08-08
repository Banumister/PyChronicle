from src.ui.terminal import TerminalUI


ui = TerminalUI()

print("=" * 50)
print("TERMINAL UI TEST")
print("=" * 50)

print("\nInitial Event")
ui.display_event(ui.engine.current())
ui.display_state()


# Find events that contain recorded variables.
variable_events = [
    event for event in ui.engine.events
    if event.get("variable") is not None
]


if variable_events:
    first_variable_event = variable_events[0]

    print("\nFirst Variable Event")
    ui.engine.jump(first_variable_event["id"])
    ui.display_event(ui.engine.current())
    ui.display_state()


if len(variable_events) > 1:
    second_variable_event = variable_events[1]

    print("\nSecond Variable Event")
    ui.engine.jump(second_variable_event["id"])
    ui.display_event(ui.engine.current())
    ui.display_state()


ui.database.close()