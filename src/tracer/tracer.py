import os
from datetime import datetime

trace_events = []
event_counter = 0

TARGET_FILE = os.path.abspath("examples/runtime_demo.py")

# Store the previous local-variable snapshot for each traced frame.
_previous_locals = {}


def runtime_tracer(frame, event, arg):
    """
    Trace only the target Python file.

    Records:
    - function calls
    - executed lines
    - returns
    - changed local variables and their values
    """

    global event_counter

    filename = os.path.abspath(frame.f_code.co_filename)

    # Ignore anything outside our target program
    if filename != TARGET_FILE:
        return runtime_tracer

    if event not in ("call", "line", "return"):
        return runtime_tracer

    event_counter += 1

    current_locals = dict(frame.f_locals)

    previous_locals = _previous_locals.get(id(frame), {})

    changed_variable = None
    changed_value = None

    # Detect a newly created or changed local variable.
    for variable, value in current_locals.items():
        if variable.startswith("__"):
            continue

        previous_value = previous_locals.get(variable)

        if variable not in previous_locals or repr(value) != repr(previous_value):
            changed_variable = variable
            changed_value = value
            break

    _previous_locals[id(frame)] = current_locals

    event_data = {
        "id": event_counter,
        "event": event,
        "function": frame.f_code.co_name,
        "variable": changed_variable,
        "value": changed_value,
        "line": frame.f_lineno,
        "timestamp": datetime.now().isoformat(timespec="milliseconds"),
    }

    trace_events.append(event_data)

    if changed_variable is not None:
        print(
            f"[{event.upper():6}] "
            f"{frame.f_code.co_name:<10} "
            f"Line {frame.f_lineno} | "
            f"{changed_variable} = {changed_value}"
        )
    else:
        print(
            f"[{event.upper():6}] "
            f"{frame.f_code.co_name:<10} "
            f"Line {frame.f_lineno}"
        )

    # Clean up when the function finishes.
    if event == "return":
        _previous_locals.pop(id(frame), None)

    return runtime_tracer