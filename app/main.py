def format_linter_error(error: dict) -> dict:
    d = {
        "line" : 0,
        "column" : 0,
        "message" : 0,
        "name" : 0,
        "source": "flake8"
         }
    for i, j in error.items():
        if i == "code":
            d["name"] = j
        elif i == "line_number":
            d["line"] = j
        elif i == "column_number":
            d["column"] = j
        elif i == "text":
            d["message"] = j
    print(d)


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    pass


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass

error = {
    "code": "E501",
    "filename": "./source_code_2.py",
    "line_number": 18,
    "column_number": 80,
    "text": "line too long (99 > 79 characters)",
    "physical_line": '    return f"I like to filter, rounding, doubling, '
    "store and decorate numbers: {', '.join(items)}!\"",
}
format_linter_error(error)