def format_linter_error(error: dict) -> dict:
    return {
        new_key: error.get(old_key, "flake8")
        for new_key, old_key in [
            ("line", "line_number"),
            ("column", "column_number"),
            ("message", "text"),
            ("name", "code"),
            ("source", "source")
        ]
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(err) for err in errors],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path, file_errors)
        for file_path, file_errors in linter_report.items()
    ]
