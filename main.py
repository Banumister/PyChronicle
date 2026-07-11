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