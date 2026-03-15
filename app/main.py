def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "path": file_path,
        "errors": [format_linter_error(err) for err in errors],
        "status": "passed" if not errors else "failed",
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(fp, errs) for fp, errs in linter_report.items()]
