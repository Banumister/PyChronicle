class Timeline:
    """
    Timeline navigator for execution events.
    """

    def __init__(self, events):
        self.events = events
        self.current_index = 0

    def current(self):
        if not self.events:
            return None

        return self.events[self.current_index]

    def next(self):
        if self.current_index < len(self.events) - 1:
            self.current_index += 1

        return self.current()

    def previous(self):
        if self.current_index > 0:
            self.current_index -= 1

        return self.current()

    def jump(self, index):
        if 0 <= index < len(self.events):
            self.current_index = index

        return self.current()

    def total_events(self):
        return len(self.events)