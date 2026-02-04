from typing import Any


def format_linter_error(error: list[dict]) -> dict[str, str | Any]:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list[dict]) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: list[dict]) -> list[dict]:
    return [format_single_linter_file(file_path, errors)
            for file_path, errors in linter_report.items()]
