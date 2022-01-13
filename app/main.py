def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8"
            }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {file_path: format_linter_error(errors)}


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": format_linter_error(error),
            "path": format_single_linter_file(linter_report),
            "status": "passed"
        }
    ]
