def format_linter_error(error: dict) -> dict:
    return {
        k: (error[v] if v in error.keys() else v)
        for k, v in {"line": "line_number",
                     "column": "column_number",
                     "message": "text",
                     "name": "code",
                     "source": "flake8"}.items()
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path=file_path, errors=errors)
        for file_path, errors in linter_report.items()
    ]
