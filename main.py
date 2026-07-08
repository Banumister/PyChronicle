import ast

from src.ast_engine.rewriter import ASTRewriter
from src.tracer.tracer import trace


def main():
    with open("examples/calculator.py", "r", encoding="utf-8") as file:
        source = file.read()

    tree = ast.parse(source)

    rewriter = ASTRewriter()
    new_tree = rewriter.visit(tree)

    ast.fix_missing_locations(new_tree)

    code = compile(new_tree, filename="<ast>", mode="exec")

    exec(code, {"trace": trace})


if __name__ == "__main__":
    main()