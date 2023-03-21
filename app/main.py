def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number", None),
        "column": error.get("column_number", None),
        "message": error.get("text", None),
        "name": error.get("code", None),
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list[dict]) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors != [] else "passed"
    }


def format_linter_report(linter_report: dict) -> list[dict]:
    return [
        format_single_linter_file(key, linter_report.get(key, None))
        for key in linter_report
    ]
