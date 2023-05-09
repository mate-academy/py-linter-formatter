def format_linter_error(error: dict) -> dict:
    return {
        "source": "flake8",
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code")
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "path": file_path,
        "status": "failed" if errors else "passed",
        "errors": [format_linter_error(i) for i in errors]
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(key, value)
            for key, value in linter_report.items()]
