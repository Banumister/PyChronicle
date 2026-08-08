from src.storage.time_travel import TimeTravelEngine


events = [
    {
        "id": 1,
        "event": "line",
        "function": "<module>",
        "variable": "x",
        "value": 10,
        "line": 1,
    },
    {
        "id": 2,
        "event": "line",
        "function": "<module>",
        "variable": "y",
        "value": 20,
        "line": 2,
    },
    {
        "id": 3,
        "event": "line",
        "function": "<module>",
        "variable": "x",
        "value": 50,
        "line": 3,
    },
    {
        "id": 4,
        "event": "line",
        "function": "<module>",
        "variable": "z",
        "value": 100,
        "line": 4,
    },
]


engine = TimeTravelEngine(events)


print("=" * 60)
print("TIME-TRAVEL ENGINE TEST")
print("=" * 60)


print("\nCurrent Event")
print(engine.current())

print("\nCurrent State")
print(engine.state())


print("\nNext Event")
print(engine.next())

print("\nState After Next")
print(engine.state())


print("\nNext Event")
print(engine.next())

print("\nState After Next")
print(engine.state())


print("\nPrevious Event")
print(engine.previous())

print("\nState After Previous")
print(engine.state())


print("\nJump to Event 4")
print(engine.jump(4))

print("\nState at Event 4")
print(engine.state())


print("\nDirect State Reconstruction at Event 2")
print(engine.state_at(2))