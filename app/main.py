def format_linter_error(errors: dict) -> dict:
    return {
        "line": errors["line_number"],
        "column": errors["column_number"],
        "message": errors["text"],
        "name": errors["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(el) for el in errors],
        "path": file_path,
        "status": "passed" if not errors else "failed"}


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(path, errors)
        for path, errors in linter_report.items()
    ]
