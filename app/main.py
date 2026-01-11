def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number", 0),
        "column": error.get("column_number", 0),
        "message": error.get("text", "UNKNOWN"),
        "name": error.get("code", ""),
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(e) for e in errors],
        "path": file_path,
        "status": ("failed" if len(errors) > 0 else "passed"),
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file_path, errors)
            for file_path, errors in linter_report.items()]
