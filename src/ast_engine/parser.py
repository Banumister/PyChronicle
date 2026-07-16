import ast


class ASTParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = None

    def parse(self):
        """Read and parse the Python source file."""
        with open(self.file_path, "r", encoding="utf-8") as file:
            source_code = file.read()

        self.tree = ast.parse(source_code)
        return self.tree

    def print_ast(self):
        """Print the Abstract Syntax Tree."""
        if self.tree is None:
            raise ValueError("Parse a file first.")

        print(ast.dump(self.tree, indent=4))

    def find_assignments(self):
        """Return all variable assignments."""
        if self.tree is None:
            raise ValueError("Parse a file before searching assignments.")

        assignments = []

        for node in ast.walk(self.tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        assignments.append({
                            "variable": target.id,
                            "line": node.lineno,
                            "type": type(node.value).__name__
                        })

        return assignments