from src.storage.state_reconstructor import StateReconstructor


events = [
    {
        "id": 1,
        "variable": "x",
        "value": 10
    },
    {
        "id": 2,
        "variable": "y",
        "value": 20
    },
    {
        "id": 3,
        "variable": "x",
        "value": 50
    },
    {
        "id": 4,
        "variable": "z",
        "value": 100
    }
]


reconstructor = StateReconstructor()

print("State at Event 2")
print(reconstructor.reconstruct(events, 2))

print()

print("State at Event 4")
print(reconstructor.reconstruct(events, 4))