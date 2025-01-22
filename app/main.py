def format_linter_error(error: dict) -> dict:

    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8"
    }

def format_single_linter_file(file_path: str, errors: list) -> dict:
    format_errors = [format_linter_error(error) for error in errors]
    return {
    "errors": format_errors,
        "path": file_path,
        "status": "failed" if format_errors else "passed"
    }

def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file_path, file_errors)
            for file_path,file_errors in linter_report.items()]
