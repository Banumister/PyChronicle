import os
from datetime import datetime

trace_events = []
event_counter = 0

TARGET_FILE = os.path.abspath("examples/runtime_demo.py")


def runtime_tracer(frame, event, arg):
    """
    Trace only the target Python file.
    """

    global event_counter

    filename = os.path.abspath(frame.f_code.co_filename)

    # Ignore anything outside our target program
    if filename != TARGET_FILE:
        return runtime_tracer

    if event not in ("call", "line", "return"):
        return runtime_tracer

    event_counter += 1

    event_data = {
        "id": event_counter,
        "event": event,
        "function": frame.f_code.co_name,
        "line": frame.f_lineno,
        "timestamp": datetime.now().isoformat(timespec="milliseconds"),
    }

    trace_events.append(event_data)

    print(
        f"[{event.upper():6}] "
        f"{frame.f_code.co_name:<10} "
        f"Line {frame.f_lineno}"
    )

    return runtime_tracer