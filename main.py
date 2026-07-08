import sys

from src.tracer.tracer import runtime_tracer, trace_events
from src.storage.database import TraceDatabase
from src.storage.timeline import Timeline


def main():

    # Create database
    database = TraceDatabase()
    database.create_tables()
    database.clear_events()

    # Read target program
    with open("examples/runtime_demo.py", "r", encoding="utf-8") as file:
        source = file.read()

    # Compile target program
    compiled_code = compile(
        source,
        "examples/runtime_demo.py",
        "exec"
    )

    # Start tracing
    sys.settrace(runtime_tracer)

    # Execute program
    exec(compiled_code, {})

    # Stop tracing
    sys.settrace(None)

    print()
    print("=" * 60)
    print("RUNTIME EVENTS")
    print("=" * 60)

    for event in trace_events:
        print(event)

    print()
    print("Saving events to SQLite...")

    for event in trace_events:
        database.insert_runtime_event(event)

    print()
    print("=" * 60)
    print("DATABASE CONTENT")
    print("=" * 60)

    rows = database.fetch_events()

    for row in rows:
        print(row)

    # -----------------------------
    # Timeline Demo
    # -----------------------------

    events = database.fetch_event_objects()

    timeline = Timeline(events)

    print()
    print("=" * 60)
    print("TIMELINE DEMO")
    print("=" * 60)

    print("\nCurrent Event")
    print(timeline.current())

    print("\nNext Event")
    print(timeline.next())

    print("\nNext Event")
    print(timeline.next())

    print("\nPrevious Event")
    print(timeline.previous())

    print("\nJump to Event 8")
    print(timeline.jump(7))

    database.close()


if __name__ == "__main__":
    main()