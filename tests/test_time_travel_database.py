from src.storage.database import TraceDatabase
from src.storage.time_travel import TimeTravelEngine


db = TraceDatabase(":memory:")
db.create_tables()


events = [
    {
        "event": "line",
        "function": "<module>",
        "variable": "x",
        "value": 10,
        "line": 1,
        "timestamp": "test"
    },
    {
        "event": "line",
        "function": "<module>",
        "variable": "y",
        "value": 20,
        "line": 2,
        "timestamp": "test"
    },
    {
        "event": "line",
        "function": "<module>",
        "variable": "x",
        "value": 50,
        "line": 3,
        "timestamp": "test"
    }
]


for event in events:
    db.insert_runtime_event(event)


stored_events = db.fetch_event_objects()

print("=" * 60)
print("DATABASE → TIME-TRAVEL INTEGRATION TEST")
print("=" * 60)

print("\nStored Events")
for event in stored_events:
    print(event)


engine = TimeTravelEngine(stored_events)

print("\nCurrent Event")
print(engine.current())

print("\nCurrent State")
print(engine.state())

print("\nNext Event")
print(engine.next())

print("\nState After Next")
print(engine.state())

print("\nJump to Event 3")
print(engine.jump(3))

print("\nState at Event 3")
print(engine.state())

db.close()