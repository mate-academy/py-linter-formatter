def format_linter_error(error: dict) -> dict:

    return {
        "name": error.get("code"),
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:

    return {
        "errors": [format_linter_error(err_point) for err_point in errors],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:

    return [
        format_single_linter_file(key, val)
        for key, val in linter_report.items()
    ]
