def format_linter_error(error: dict) -> dict:
    # formats a single error
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # formats all errors for a particular file
    # adds the path key — path to the file,
    # the status key — "failed" if there are errors,
    # "passed" if there are no errors
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed"
        if len(errors) != 0
        else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    # formats all errors for all report files
    return [
        format_single_linter_file(key, value)
        for key, value in linter_report.items()
    ]
