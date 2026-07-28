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
        Reconstruct the variable state up to target_event_id.

        Parameters
        ----------
        events : list
            List of runtime events.
        target_event_id : int
            Event ID up to which the state is reconstructed.

        Returns
        -------
        dict
            Snapshot of reconstructed variables.
        """

        self.state.reset()

        for event in events:

            if event["id"] > target_event_id:
                break

            variable = event.get("variable")
            value = event.get("value")

            if variable is not None:
                self.state.assign(variable, value)

        return self.state.snapshot()