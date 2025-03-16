def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line"],
        "error": error["message"]
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    if not errors:
        return {file_path: []}

    formatted_errors = [format_linter_error(error) for error in errors]
    return {file_path: formatted_errors}


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file, errors)
        for file, errors in linter_report.items()
    ]
