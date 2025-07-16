from typing import Any


def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }

def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,  # Use file_path directly as it's the input path
        "status": "failed" if any(format_linter_error(error) != {} for error in errors) else "passed"
    }


def format_linter_report(linter_report: dict) -> dict[Any, dict[str, list[dict] | str | Any]]:
    return {
        key: {
            "errors": [format_linter_error(char) for char in value],
            "path": key,
            "status": "passed" if not value else "failed",
        }
        for key, value in linter_report.items()
    }

