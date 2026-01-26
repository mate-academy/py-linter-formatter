def format_linter_error(error: dict) -> dict:
    return {"line": error.get("line_number", 0),
            "column": error.get("column_number", 0),
            "message": error.get("text", 0),
            "name": error.get("code", 0),
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file_path=key, errors=value)
            for key, value in linter_report.items()]
