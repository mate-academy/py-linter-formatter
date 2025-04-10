def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }

def format_single_linter_file(filename: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": filename,
        "status": "passed" if not errors else "failed"
    }

def format_linter_report(reports: dict) -> list:
    return [format_single_linter_file(filename, errors) for filename, errors in reports.items()]
