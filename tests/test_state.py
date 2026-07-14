from src.storage.state import ProgramState

state = ProgramState()

state.assign("x", 10)
state.assign("y", 20)

print(state.snapshot())

state.assign("x", 50)

print(state.snapshot())

print(state.get("x"))

state.reset()

print(state.snapshot())