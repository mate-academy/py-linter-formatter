def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"] if "line_number" in error else None,
        "column": error["column_number"] if "column_number" in error else None,
        "message": error["text"] if "text" in error else None,
        "name": error["code"] if "code" in error else None,
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors" : [format_linter_error(errors[i]) for i in range(len(errors))],
        "path" : file_path,
        "status" : " ".join(["failed" if len([errors]) > 0 else "passed"])
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(keys, errors) for keys, errors in linter_report.items()]

report_file = {
    "./test_source_code_2.py": [],
    "./source_code_2.py":
        [
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
}

print(format_linter_report(report_file))

