class ProgramState:
    """
    Stores the current reconstructed program state.
    """

    def __init__(self):
        self.variables = {}

    def assign(self, variable, value):
        """
        Store or update a variable.
        """
        self.variables[variable] = value

    def get(self, variable):
        """
        Return the value of a variable.
        """
        return self.variables.get(variable)

    def snapshot(self):
        """
        Return a copy of the current program state.
        """
        return dict(self.variables)

    def reset(self):
        """
        Clear all stored variables.
        """
        self.variables.clear()