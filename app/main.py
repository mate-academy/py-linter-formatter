def format_linter_error(error: dict) -> dict:
    return {  # Not sure if dict comprehension is supposed to be used here.
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {  # Neither am I sure if I should use comprehension here...
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [  # Oh, finally. This one is clear!
        format_single_linter_file(file, linter_report[file])
        for file in linter_report
    ]
