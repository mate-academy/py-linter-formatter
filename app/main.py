def format_linter_error(error: dict) -> dict:
    return {
        key: error[error_key]
        for key, error_key in (
            ("name", "code"),
            ("message", "text"),
            ("column", "column_number"),
            ("line", "line_number"),
        )
    } | {"source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if len(errors) > 0 else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file_path, errors)
            for file_path, errors in linter_report.items()]
