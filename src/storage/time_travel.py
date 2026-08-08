from src.storage.state_reconstructor import StateReconstructor


class TimeTravelEngine:
    """
    Provides time-travel navigation over recorded execution events.

    The engine does not execute the program again.
    It navigates through recorded events and reconstructs
    the program state at the selected execution point.
    """

    def __init__(self, events):
        self.events = sorted(events, key=lambda event: event["id"])
        self.current_index = 0 if self.events else -1
        self.reconstructor = StateReconstructor()

    def current(self):
        """
        Return the current execution event.
        """
        if self.current_index == -1:
            return None

        return self.events[self.current_index]

    def next(self):
        """
        Move to the next execution event.
        """
        if not self.events:
            return None

        if self.current_index < len(self.events) - 1:
            self.current_index += 1

        return self.current()

    def previous(self):
        """
        Move to the previous execution event.
        """
        if not self.events:
            return None

        if self.current_index > 0:
            self.current_index -= 1

        return self.current()

    def jump(self, event_id):
        """
        Jump directly to an event using its event ID.
        """
        for index, event in enumerate(self.events):
            if event["id"] == event_id:
                self.current_index = index
                return event

        return None

    def state(self):
        """
        Reconstruct the program state at the current event.
        """
        current_event = self.current()

        if current_event is None:
            return {}

        return self.reconstructor.reconstruct(
            self.events,
            current_event["id"]
        )

    def state_at(self, event_id):
        """
        Reconstruct the program state at a specific event ID.
        """
        event = self.jump(event_id)

        if event is None:
            return None

        return self.reconstructor.reconstruct(
            self.events,
            event_id
        )