def format_linter_error(error: dict) -> dict:
    error_formated = {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }

    return error_formated


def format_single_linter_file(file_path: str, errors: list) -> dict:
    linter_filer_formated = {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if len(errors) > 0 else "passed"
    }

    return linter_filer_formated


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass
