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
        "errors": [format_linter_error(e) for e in errors],
        "path": file_path,
        "status": "failed" if errors else "passed",
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(path, errs)
            for path, errs in linter_report.items()]
