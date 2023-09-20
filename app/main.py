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
        "errors": [format_linter_error(error=error) for error in errors],
        "path": file_path,
        "status": "passed" if not errors else "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path=file, errors=report)
        for file, report in linter_report.items()
    ]


simplified format_single_linter_file function, also changed variable name in format_linter_report function