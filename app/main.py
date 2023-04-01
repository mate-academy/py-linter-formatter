"""Contains functions to format flake8 report for a file."""


LINTER_NAME = "flake8"


def format_linter_error(error: dict) -> dict:
    """Format error to a linter specific report.

    Args:
        error - the error information

    Returns:
        A dict with formatted error
    """
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": LINTER_NAME
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    """Format single file error to a linter specific report.

    Args:
        file_path - a file path
        errors - file formatting errors

    Returns:
        A dict with file path, linter status, and a list of errors
    """
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if len(errors) > 0 else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    """Format multiple files error to a linter specific report.

    Args:
        linter_report - files with errors

    Returns:
        A list of dicts with file path, linter status, and a list of errors
    """
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
