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