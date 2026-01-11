def format_linter_error(error: dict) -> dict:
    return {
        new_key: error[old_key] for old_key, new_key
        in {
            "line_number": "line",
            "column_number": "column",
            "text": "message",
            "code": "name"
        }.items()
        if old_key in error
    } | {"source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "passed" if not errors else "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(key, val)
        for key, val
        in linter_report.items()
    ]
