def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8"
    }


def format_single_linter_file(path: str, errors: list) -> dict:
    return {
        "path": path,
        "status": "failed" if errors else "passed",
        "errors": [format_linter_error(err) for err in errors]
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(path, errors)
        for path, errors in linter_report.items()
    ]
