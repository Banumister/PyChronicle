<<<<<<< HEAD
from ast_parser import parse_code
from tracer import start_trace

def debug_program(filename):
    print("Starting Debugger...")

    parsed_data = parse_code(filename)
    execution_history = start_trace(filename)

    return {
        "parsed_data": parsed_data,
        "execution_history": execution_history
    }


if __name__ == "__main__":
    result = debug_program("sample_code/test.py")
    print(result)
=======
from src.ast_engine.parser import ASTParser


def main():
    parser = ASTParser("examples/sample.py")

    parser.parse()

    print("=" * 50)
    print("VARIABLE ASSIGNMENTS")
    print("=" * 50)

    assignments = parser.find_assignments()

    for item in assignments:
        print(
            f"Variable: {item['variable']:<10} "
            f"Line: {item['line']:<3} "
            f"Value Type: {item['type']}"
        )


if __name__ == "__main__":
    main()
>>>>>>> 57ac040c6cec9fbe16a5725ddf5f11256954a73e
