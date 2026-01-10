import pytest


def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }
    pass


def format_single_linter_file(file_path: str, errors: list) -> dict:
    def _format_error_item(error: dict) -> dict:
        return {
            "line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8",
        }
    return {
        "errors": [_format_error_item(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors else "passed",
    }
    pass


def format_linter_report(linter_report: dict) -> list:
    def _format_error_item(error: dict) -> dict:
        return {
            "line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8",
        }
    def _format_single_file(file_path: str, errors: list) -> dict:
        return {
            "errors": [_format_error_item(error) for error in errors],
            "path": file_path,
            "status": "failed" if errors else "passed",
        }
    return [
        _format_single_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
    pass

