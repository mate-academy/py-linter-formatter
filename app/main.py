error_keys = {
    "code": "name",
    "line_number": "line",
    "column_number": "column",
    "text": "message",
    "flake8": "source",
}


def format_linter_error(error: dict) -> dict:
    return {
        value: error[key] if key in error else key
        for key, value in error_keys.items()
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if len(errors) else "passed",
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(report, linter_report[report])
        for report in linter_report
    ]
