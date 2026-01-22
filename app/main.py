def format_linter_error(error: dict) -> dict:

    return {
        "line": error.get("line_number", 18),
        "column": error.get("column_number", 80),
        "message": error.get("text", "line too long (99 > 79 characters)"),
        "name": error.get("code", "E501"),
        "source": error.get("source", "flake8")
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:

    return {"errors": [format_linter_error(error) for error in errors],
            "path": file_path,
            "status": "failed" if errors else "passed"}


def format_linter_report(linter_report: dict) -> list:

    return [format_single_linter_file(file_path, errors) for file_path,
            errors in linter_report.items()]
