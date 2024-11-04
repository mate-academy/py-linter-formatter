def format_linter_error(error: dict) -> dict:
    # Error type correction
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # Change error type by file
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "passed" if not errors else "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    # Grouping files into a list
    return [format_single_linter_file(file_name, file_errors)
            for file_name, file_errors in linter_report.items()]
