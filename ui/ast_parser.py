import ast

def parse_code(filename):
    with open(filename, "r") as file:
        tree = ast.parse(file.read())

    functions = []
    variables = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    variables.append(target.id)

    return {
        "functions": functions,
        "variables": variables
    }