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
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "path": file_path,
            "errors": [format_linter_error(e) for e in errors_list],
            "status": "failed" if errors_list else "passed"
        }
        for file_path, errors_list in linter_report.items()
    ]
