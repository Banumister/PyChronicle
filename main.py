import sys

from src.tracer.tracer import runtime_tracer, trace_events
from src.storage.database import TraceDatabase


def main():
    # Initialize database
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

    # Start runtime tracing
    sys.settrace(runtime_tracer)

    # Execute target program
    exec(compiled_code, {})

    # Stop tracing
    sys.settrace(None)

    # Display runtime events
    print("\n")
    print("=" * 60)
    print("RUNTIME EVENTS")
    print("=" * 60)

    for event in trace_events:
        print(event)

    # Save events into SQLite
    print("\nSaving events to SQLite...\n")

    for event in trace_events:
        database.insert_runtime_event(event)

    # Display database contents
    print("=" * 60)
    print("DATABASE CONTENT")
    print("=" * 60)

    rows = database.fetch_events()

    for row in rows:
        print(row)

    # Close database
    database.close()


if __name__ == "__main__":
    main()