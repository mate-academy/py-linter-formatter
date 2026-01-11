def format_linter_error(error: dict) -> dict:
    # Format a single linter error into the standard dictionary
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # Format all errors for a single file
    # Use the helper function format_linter_error to avoid duplicated logic
    return {
        # format each error
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,  # file path
        "status": "passed" if not errors else "failed"  # file status
    }


def format_linter_report(linter_report: dict) -> list:
    # Format all files in the linter report
    # Reuse format_single_linter_file to avoid duplicating dict creation
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
