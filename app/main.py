def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number", 0),
        "column": error.get("column_number", 0),
        "message": error.get("text", "Unknown error"),
        "name": error.get("code", "Unknown"),
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "path": file_path,
        "errors": [format_linter_error(error) for error in errors],
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
