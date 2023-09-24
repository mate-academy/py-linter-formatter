def format_linter_error(error: dict) -> dict:

    formatted_error = {
        "file_path": error.get("file_path", ""),
        "line": error.get("line", ""),
        "message": error.get("message", ""),

    }
    return formatted_error


def format_single_linter_file(file_path: str, errors: list) -> dict:

    formatted_file = {
        "file_path": file_path,
        "errors": [format_linter_error(error) for error in errors],
    }
    return formatted_file


def format_linter_report(linter_report: dict) -> list:

    formatted_report = []
    for file_path, errors in linter_report.items():
        formatted_report.append(format_single_linter_file(file_path, errors))
    return formatted_report
