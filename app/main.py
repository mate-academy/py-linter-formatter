def format_linter_error(error: dict) -> dict:
    # """ formats a single error dictionary """
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # """ formats all errors for a particular file
    # and adds the path key — path to the file,
    # and the status key — "failed" if there are errors,
    # "passed" if there are no errors:
    # """
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors else "passed",
    }


def format_linter_report(linter_report: dict) -> list:
    # """ formats all errors for all report files: """
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
