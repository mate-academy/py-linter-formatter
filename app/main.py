from typing import Any

def format_linter_error(error: dict) -> dict[str, str | Any]:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }

def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(err) for err in errors],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }

def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": format_single_linter_file(path, err)["errors"],
            "path": path,
            "status": format_single_linter_file(path, err)["status"]
        } for path, err in linter_report.items()
    ]