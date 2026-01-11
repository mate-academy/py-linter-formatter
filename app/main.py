def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number", "no INFO"),
        "column": error.get("column_number", "no INFO"),
        "message": error.get("text", "no INFO"),
        "name": error.get("code", "no INFO"),
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(path, errors)
        for path, errors in linter_report.items()
    ]
