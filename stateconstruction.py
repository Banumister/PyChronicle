class ProgramState:

    def __init__(self):
        self.variables = {}
        self.snapshots = []

    def assign(self, variable, value):
        self.variables[variable] = value
        self.snapshots.append(dict(self.variables))

    def get(self, variable):
        return self.variables.get(variable)

    def snapshot(self):
        return dict(self.variables)

    def get_snapshots(self):
        return self.snapshots

    def replay_variable(self, variable):
        history = []

        for snap in self.snapshots:
            if variable in snap:
                history.append(snap[variable])

        return history

    def variable_at_step(self, variable, step):
        if 0 <= step < len(self.snapshots):
            return self.snapshots[step].get(variable)

        return None

    def reconstruct_state(self, step):
        if 0 <= step < len(self.snapshots):
            self.variables = dict(self.snapshots[step])
            return self.variables

        return None

    def reset(self):
        self.variables.clear()
        self.snapshots.clear()
