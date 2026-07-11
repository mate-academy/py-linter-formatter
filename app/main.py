def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number"),
        "message": error.get("text"),
        "column": error.get("column_number"),
        "name": error.get("code"),
        "Source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "file_path": file_path,
        "errors": [format_linter_error(error) for error in errors]
    }
    pass


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file_path, errors) for file_path, errors in linter_report.items()]
