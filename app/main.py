def format_linter_error(error: dict) -> dict:
    # Format a single linter error into a simple form
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }

def format_single_linter_file(file_path: str, errors: list) -> dict:
    # Format linter errors for one file and return a dictionary with formatted error data for the file
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }

def format_linter_report(linter_report: dict) -> list:
    # Format linter results individually and return a list with formatting results for each file
    return [format_single_linter_file(file_path, errors) for file_path, errors in linter_report.items()]
