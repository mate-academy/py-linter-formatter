def format_linter_error(error: dict) -> dict:
    return {
        key: value
        for key, value in {"line": error["line_number"],
                           "column": error["column_number"],
                           "message": error["text"],
                           "name": error["code"],
                           "source": "flake8"}.items()}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        key: value
        for key, value in {"errors": [format_linter_error(error)
                                      for error in errors],
                           "path": file_path,
                           "status": "failed" if errors else "passed"}.items()}


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path, error)
        for file_path, error in linter_report.items()
    ]
