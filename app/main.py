def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error)
                   for error in errors],
        "path": file_path,
        "status": ("failed" if errors else "passed")}


def format_linter_report(linter_report: dict) -> list:
    return [{
        "errors": [format_linter_error(error)
                   if error else "" for error in linter_value],
        "path": linter_key,
        "status": ("failed" if linter_value else "passed")}
        for linter_key, linter_value in linter_report.items()]
