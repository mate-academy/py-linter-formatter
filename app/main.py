def format_linter_error(error: dict) -> dict:
    # white your code here
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # white your code here
    return {
        "errors": [format_linter_error(err) for err in errors],
        "path": file_path,
        "status": "passed" if errors == [] else "failed",
    }


def format_linter_report(linter_report: dict) -> list:
    # white your code here
    return [
        format_single_linter_file(key_path, errors_value)
        for key_path, errors_value in linter_report.items()
    ]
