def format_linter_error(error: dict) -> dict:
    """
    Formats a single error.
    :param error: Error which should be formatted.
    :return:  Dict of the error.
    """
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    """
    Formats all errors for a particular file and adds the path key —
    path to the file, and the status key — "failed" if there are errors,
    "passed" if there are no errors.
    :param file_path: Path to the file.
    :param errors: Errors list.
    :return: The dict of errors, path and status.
    """
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "passed" if errors == [] else "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    """
    Formats all errors for all report files.
    :param linter_report: Report with errors.
    :return: The list of dicts of errors, path and status.
    """
    return [
        format_single_linter_file(path, errors)
        for path, errors in linter_report.items()
    ]
