def format_linter_error(error: dict) -> dict:

    return {
        value: (error[key] if key in error else "flake8")
        for key, value in {
            "line_number": "line",
            "column_number": "column",
            "text": "message",
            "code": "name",
            "source": "source"
        }.items()
    } if error else error


def format_single_linter_file(file_path: str, errors: list) -> dict:

    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:

    return [
        format_single_linter_file(key, value)
        for key, value in linter_report.items()
    ]
