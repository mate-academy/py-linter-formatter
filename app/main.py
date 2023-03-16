from typing import Any


def format_linter_error(error: dict[str, str]) -> dict[str, str]:
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8"
    }


def format_single_linter_file(
    file_path: str,
    errors: list[dict[str, str]]
) -> dict[str, Any]:
    return {
        "errors": [
            format_linter_error(error) for error in errors
        ],
        "path": file_path,
        "status": "passed" if not errors else "failed"
    }


def format_linter_report(
    linter_report: dict[str, list[dict[str, str]]]
) -> list[dict[str, Any]]:
    return [
        format_single_linter_file(path, error_list)
        for path, error_list in linter_report.items()
    ]
