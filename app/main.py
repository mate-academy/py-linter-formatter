def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"] if "line_number" in error else None,
        "column": error["column_number"] if "column_number" in error else None,
        "message": error["text"] if "text" in error else None,
        "name": error["code"] if "code" in error else None,
        "source": "flake8"
    }
    pass


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [] if not errors
        else [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "passed" if not errors else "failed"
    }
    pass


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
    pass
