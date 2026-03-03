def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8",
    }

def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "path": file_path,
        "errors": [format_linter_error(error) for error in errors],
        "status": "failed" if errors else "passed"
    }

def format_linter_report(linter_report: dict) -> list:
    # Using format_single_linter_file function to avoid redundant code
    return [format_single_linter_file(file_path, errors) for file_path, errors in linter_report.items()]
