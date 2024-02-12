def format_linter_error(error: dict) -> dict:
    # write your code here
    return {"line": error["line_number"], "column": error["column_number"],
            "message": error["text"], "name": error["code"], "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    return \
        {
        "errors": [{"line": item["line_number"], "column": item["column_number"],
                    "message": item["text"], "name": item["code"], "source": "flake8"}
                   for item in errors],
            "path": file_path, "status": "failed"
    }

errors = [
    {
        "code": "E501",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 80,
        "text": "line too long (99 > 79 characters)",
        "physical_line": '    return f"I like to filter, rounding, doubling, '
        "store and decorate numbers: {', '.join(items)}!\"",
    },
    {
        "code": "W292",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 100,
        "text": "no newline at end of file",
        "physical_line": '    return f"I like to filter, rounding, doubling, '
        "store and decorate numbers: {', '.join(items)}!\"",
    },
]


print(format_single_linter_file("./source_code_2.py", errors))

def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass
