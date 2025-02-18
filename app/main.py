def format_linter_error(error: dict) -> dict:
    """
    Formats a single linter error.

    :param error: Dictionary containing linter error details.
    :return: Formatted dictionary.
    """
    return {
        "line": error.get("line", 0),
        "column": error.get("column", 0),
        "message": error.get("message", "Unknown error"),
        "rule": error.get("rule", "Unknown rule"),
        "severity": error.get("severity", "warning")
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    """
    Formats linter errors for a single file.

    :param file_path: Path to the file being linted.
    :param errors: List of linter errors.
    :return: Dictionary with formatted errors.
    """
    return {
        "file": file_path,
        "errors": [format_linter_error(error) for error in errors]
    }


def format_linter_report(linter_report: dict) -> list:
    """
    Formats the overall linter report.

    :param linter_report: Dictionary containing linter results.
    :return: List of formatted file error reports.
    """
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
