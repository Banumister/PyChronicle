from src.storage.state import ProgramState


class StateReconstructor:
    """
    Reconstructs the program state by replaying
    variable assignment events.
    """

    def __init__(self):
        self.state = ProgramState()

    def reconstruct(self, events, target_event_id):
        """
        Reconstruct the variable state up to the given event ID.
        """

        self.state.reset()

        if not events:
            return self.state.snapshot()

        for event in events:
            if event["id"] > target_event_id:
                break

            variable = event.get("variable")
            value = event.get("value")

            if variable is not None:
                self.state.assign(variable, value)

        return self.state.snapshot()