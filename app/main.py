from typing import Any


def format_linter_error(error: dict[str, Any]) -> dict[str, Any]:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }


def format_single_linter_file(
    file_path: str,
    errors: list[dict[str, Any]],
) -> dict[str, Any]:
    formatted_errors = [
        format_linter_error(error)
        for error in errors
    ]

    return {
        "path": file_path,
        "status": "failed" if len(errors) > 0 else "passed",
        "errors": formatted_errors,
    }


def format_linter_report(
    linter_report: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
