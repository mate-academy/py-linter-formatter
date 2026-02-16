def format_linter_error(error: dict) -> dict:
    return {
        new_key: error[old_key]
        for new_key, old_key in [
            ("line", "line_number"),
            ("column", "column_number"),
            ("message", "text"),
            ("name", "code"),
        ]
    } | {"source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if len(errors) > 0
        else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file_path, errors)
            for file_path, errors in linter_report.items()]
