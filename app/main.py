def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors_list: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors_list],
        "path": file_path,
        "status": "failed" if errors_list else "passed"
    }


def format_linter_report(report_file: dict) -> dict:
    return [
        format_single_linter_file(file_path, errors_list)
        for file_path, errors_list in report_file.items()
    ]
