import sys
execution_history = []

def trace(frame, event, arg):
    if event == "line":
        execution_history.append({
            "line": frame.f_lineno,
            "function": frame.f_code.co_name,
            "file": frame.f_code.co_filename
        })
    return trace


def start_trace(program):
    execution_history.clear()

    sys.settrace(trace)

    with open(program) as file:
        code = file.read()

    exec(code, {})

    sys.settrace(None)

    return execution_history