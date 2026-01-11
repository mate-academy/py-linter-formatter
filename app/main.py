from typing import TypedDict, List


class ErrorDict(TypedDict):
    code: str
    filename: str
    line_number: int
    column_number: int
    text: str
    physical_line: str


class FormattedError(TypedDict):
    line: int
    column: int
    message: str
    name: str
    source: str


class FormattedFile(TypedDict):
    errors: List[FormattedError]
    path: str
    status: str


def format_linter_error(error: ErrorDict) -> FormattedError:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path, errors) for file_path,
        errors in linter_report.items()
    ]
