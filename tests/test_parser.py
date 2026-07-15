import ast
import pytest
from src.ast_engine.parser import ASTParser


def test_parse_valid_python(tmp_path):
    # Create a temporary Python file
    code = "x = 10\ny = 20"
    file = tmp_path / "sample.py"
    file.write_text(code)

    parser = ASTParser(str(file))
    tree = parser.parse()

    assert isinstance(tree, ast.Module)


def test_find_assignments(tmp_path):
    code = "x = 10\ny = 'Hello'"
    file = tmp_path / "sample.py"
    file.write_text(code)

    parser = ASTParser(str(file))
    parser.parse()

    assignments = parser.find_assignments()

    assert len(assignments) == 2
    assert assignments[0]["variable"] == "x"
    assert assignments[1]["variable"] == "y"


def test_print_ast_without_parse(tmp_path):
    file = tmp_path / "sample.py"
    file.write_text("x = 10")

    parser = ASTParser(str(file))

    with pytest.raises(ValueError):
        parser.print_ast()


def test_find_assignments_without_parse(tmp_path):
    file = tmp_path / "sample.py"
    file.write_text("x = 10")

    parser = ASTParser(str(file))

    with pytest.raises(ValueError):
        parser.find_assignments()