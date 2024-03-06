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
        "errors": [],
        "path": file_path,
        "status": "passed"
    } if not errors else {
        "errors": [format_linter_error(err) for err in errors],
        "path": file_path,
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(report, linter_report[report])
        for report in linter_report
    ]
