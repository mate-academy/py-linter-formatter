def format_linter_error(error: dict) -> dict:
    if not isinstance(error, dict):
        return {
            "line": None,
            "column": None,
            "message": "Invalid error format",
            "name": None,
            "source": "flake8",
        }

    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors) -> dict:
    safe_errors = [
        format_linter_error(error)
        for error in (errors or [])
    ]

    return {
        "errors": safe_errors,
        "path": file_path,
        "status": "failed" if safe_errors else "passed",
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in (linter_report or {}).items()
    ]
