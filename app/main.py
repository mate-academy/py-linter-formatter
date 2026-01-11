def format_linter_error(old_error: dict) -> dict:
    return {
        "line": old_error["line_number"],
        "column": old_error["column_number"],
        "message": old_error["text"],
        "name": old_error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(old_error) for old_error in errors],
        "path": file_path,
        "status": "failed" if len(errors) > 0 else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file, errors)
        for file, errors in linter_report.items()
    ]
