from typing import Any


# Format a linter error data into another dictionary format
def format_linter_error(error: dict[str, Any]) -> dict[str, Any]:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


# Apply format_linter_error() for each error from list
# Return report for a single file with path,
# list of formatted errors and status (passed/failed)
def format_single_linter_file(file_path: str,
                              errors: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "errors": [format_linter_error(error=e) for e in errors],
        "path": file_path,
        "status": "failed" if len(errors) > 0 else "passed"
    }


# Apply format_single_linter_file() for each file from report
# Return linter report for multiple files
def format_linter_report(
    linter_report: dict[str, list[dict[str, Any]]]
) -> list[dict[str, Any]]:
    return [
        format_single_linter_file(file_path=file_path, errors=errors)
        for file_path, errors in linter_report.items()
    ]
